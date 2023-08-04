nt_loop()
tasks = [fetch_page("https://google.com") for i in range(50)]
start = time.time()
loop.run_until_complete(asyncio.gather(*tasks))
print(f"All pages took {time.time() - start} seconds.")
