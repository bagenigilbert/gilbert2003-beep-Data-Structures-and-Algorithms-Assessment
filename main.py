import question1.question1
import question2.question2
import question3.question3

expression1 = "([]{})"
expression2 = "([)]"
print(question1.is_balanced(expression1))
print(question1.is_balanced(expression2))

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = question2.remove_duplicates(input_sequence)
print(result)

sentence = "This is a test sentence. This sentence is a test."
result = question3.word_frequency(sentence)
print(result)