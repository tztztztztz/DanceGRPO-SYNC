import hpsv2


print("Testing SD with HPSv2")
prompt = "a photo of an astronaut riding a horse on mars"
sd_image_path = "astronaut_rides_horse.png" 
result = hpsv2.score(sd_image_path, prompt, hps_version="v2.1") 
print(result)

print("Testing Flux with HPSv2")
flux_image_path = "flux-dev.png"
result = hpsv2.score(flux_image_path, prompt, hps_version="v2.1") 
print(result)