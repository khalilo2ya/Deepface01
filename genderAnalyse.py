from deepface import DeepFace
img_path_= "assets/jason_03.jpg"
actions = ['age', 'gender', 'race', 'emotion']
obj = DeepFace.analyze(img_path_, actions)
print(obj["age"]," years old ",obj["dominant_race"]," ",obj["dominant_emotion"]," ", obj["gender"])
