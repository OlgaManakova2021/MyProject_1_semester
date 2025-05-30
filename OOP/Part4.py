# Статические методы
# Декоратор @staticmethod используется для определения статического
# метода в классе. Статические методы не требуют ссылки на экземпляр
# класса (то есть они не принимают параметр self) и могут быть
# вызваны как через экземпляр класса, так и через сам класс.
# Они обычно используются для выполнения задач, которые не зависят
# от состояния экземпляра класса.

class Comment:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def merge_comments(first, second):
        return f"{first} {second}"

my_comment = Comment("My comment")

m_1 = Comment.merge_comments("Привет,","студент!")
print(m_1)
m_2 = Comment.merge_comments("Great","OK")
print(m_2)