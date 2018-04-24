import speedtest


s = speedtest.Speedtest()
s.get_best_server()
s.download()
s.upload(pre_allocate=False)
s.results.share()

print(s.results.dict())
