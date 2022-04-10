from deepface import DeepFace
import glob
pic = "image02.jpg"
files = glob.glob("assets/*")
model = "VGG-Face"
results = []
for file in files:
    result = DeepFace.verify(pic, file, model_name=model)
    results.append((file, result['distance']))
results.sort(key=lambda x: x[1])
print("Model:", model)
for file, distance in results:
    print(file, distance)
