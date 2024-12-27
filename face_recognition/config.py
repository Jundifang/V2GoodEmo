from face_recognition import *
DOMAIN: str = 'http://localhost'
PORT: str = '8000'
API_KEY: str = 'your_face_recognition_key'

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(API_KEY)

face_collection: FaceCollection = recognition.get_face_collection()

subjects: Subjects = recognition.get_subjects()