from flask import Flask, request, jsonify, render_template
from model import load_model, predict
import os
from visualization import plot_results  # Импортируем функцию для визуализации

app = Flask(__name__)
model = load_model()

# Примерные данные для графика
models = ['VGG', 'YOLO', 'MobileNet']
accuracies = [85, 90, 88]  # Примерные данные точности
plot_results(models, accuracies)  # Создание графика


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict_route():
    if 'image' not in request.files:
        return jsonify({'status': 'error', 'message': 'No image provided.'}), 400

    image = request.files['image']
    image_path = os.path.join('static', image.filename)
    image.save(image_path)

    results = predict(model, image_path)
    return jsonify({'status': 'success', 'results': results})


if __name__ == '__main__':
    app.run(debug=True)