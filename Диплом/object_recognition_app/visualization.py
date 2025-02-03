import matplotlib.pyplot as plt

def plot_results(models, accuracies):
    plt.figure(figsize=(10, 6))
    plt.bar(models, accuracies, color=['blue', 'orange', 'green', 'red'])
    plt.xlabel('Models')
    plt.ylabel('Accuracy (%)')
    plt.title('Model Performance Comparison')
    plt.ylim(0, 100)
    plt.grid(axis='y')

    # Добавление значений над столбиками
    for i, v in enumerate(accuracies):
        plt.text(i, v + 1, str(v), ha='center')

    plt.savefig('static/model_performance.png')  # Сохранение графика в папку static
    plt.close()

# Пример использования
if __name__ == "__main__":
    models = ['VGG', 'YOLO', 'MobileNet']
    accuracies = [85, 90, 88]  # Примерные данные точности
    plot_results(models, accuracies)