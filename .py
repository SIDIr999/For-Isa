# Quiz Game на Python

# Вопросы и ответы
questions = [
    {
        "question": "Сколько будет 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Столица Франции?",
        "options": ["Берлин", "Мадрид", "Париж", "Рим"],
        "answer": "Париж"
    },
    {
        "question": "Какой язык используется для создания сайтов?",
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": "HTML"
    }
]

# Старт
score = 0
print("Добро пожаловать в Quiz Game!\n")

# Игра
for i, q in enumerate(questions):
    print(f"Вопрос {i+1}: {q['question']}")
    for idx, option in enumerate(q['options'], 1):
        print(f"{idx}. {option}")

    user_input = input("Выбери вариант (1-4): ")

    # Проверка
    if q['options'][int(user_input)-1] == q['answer']:
        print("✅ Правильно!\n")
        score += 1
    else:
        print(f"❌ Неправильно! Правильный ответ: {q['answer']}\n")

# Итог
print(f"Игра окончена! Твой результат: {score} из {len(questions)}.")
