from thispersondoesnotexist import get_online_person
from time import sleep
# picture = get_online_person()  # bytes representation of the image

# Save to a file
from thispersondoesnotexist import save_picture
# save_picture(picture, "fakes/a_beautiful_person.jpg")
# If no filename is provided, one will be generated using the checksum of the picture
# save_picture(picture)

N = 5 # number of images to download

for i in range(N):
    picture = get_online_person()
    save_picture(picture, f"fakes/fake_{i}.jpg")
    print(f"Saved {i}")
    sleep(3)