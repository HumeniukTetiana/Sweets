import time
import requests
import psutil
import pandas as pd
import plotly.express as px
from concurrent.futures import ThreadPoolExecutor, as_completed
from django.http import JsonResponse
from django.shortcuts import render


def db_performance_test(request):
    num_requests = int(request.GET.get('num_requests', 5))
    num_threads_list = [1, 2, 4, 8, 16]
    url = 'http://localhost:8000/statistic/ingredients-products-dashboard/'
    all_results = []

    def make_request():
        start_time = time.time()
        response = requests.get(url)
        elapsed = time.time() - start_time
        return elapsed

    for num_threads in num_threads_list:
        results = []
        cpu_usages = []
        memory_usages = []

        start_cpu = psutil.cpu_percent(interval=None)
        start_mem = psutil.virtual_memory().used / (1024 ** 2)

        start_global = time.time()
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(make_request) for _ in range(num_requests)]
            for future in as_completed(futures):
                try:
                    duration = future.result()
                    results.append(duration)
                    cpu_usages.append(psutil.cpu_percent(interval=None))
                    memory_usages.append(psutil.virtual_memory().used / (1024 ** 2))
                except Exception as e:
                    results.append(None)

        total_time = time.time() - start_global
        end_cpu = psutil.cpu_percent(interval=None)
        end_mem = psutil.virtual_memory().used / (1024 ** 2)

        df = pd.DataFrame({
            "request_time": results,
            "cpu_usage": cpu_usages,
            "memory_usage": memory_usages,
        })

        summary = {
            "threads_used": num_threads,
            "total_requests": num_requests,
            "total_time": total_time,
            "avg_time_per_request": df["request_time"].mean(),
            "max_cpu_usage": max(cpu_usages, default=start_cpu),
            "max_memory_usage": max(memory_usages, default=start_mem),
        }

        all_results.append(summary)

    return JsonResponse(all_results, safe=False)


def performance_dashboard(request):
    num_requests = int(request.GET.get("num_requests", 5))

    response = requests.get("http://localhost:8000/parallel_db/performance-test/", params={
        "num_requests": num_requests,
    })

    data = response.json()

    df = pd.DataFrame(data)
    fig = px.line(df, x="threads_used", y="total_time", title="Request Time by Number of Threads")
    graph_html = fig.to_html(full_html=False)

    return render(request, "performance_template.html", {
        "data": data,
        "num_requests": num_requests,
        "graph_html": graph_html,
    })
