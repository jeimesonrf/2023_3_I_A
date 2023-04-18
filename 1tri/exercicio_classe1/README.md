# EXERCÍCIO SOBRE CLASSE

## INDIVIDUAL

A atividade será entregue via arquivo no github.

Escreva uma classe cujos objetos representam alunos matriculados em uma disciplina. Cada objeto dessa classe deve guardar os seguintes dados do aluno: matrícula nome, 2 notas de prova e 1 nota de trabalho. Escreva os seguintes métodos para esta classe:
+ **media** calcula a média final do aluno (cada prova tem peso 2,5 e o trabalho tem peso 2)
+ **final** calcula quanto o aluno precisa para a prova final (retorna zero se ele não for para a final, a media deve ser maior ou igual a 4,0 e menor que 7,0)

observações:

**_media ponderada:_**

$$media = \frac{(peso1*valor1 + peso2*valor2 +peso3*valor3+...)}{peso1+peso2+peso3+..}$$

**_métodos:_**

media retorna um valor *float* 
final retorna _True_ se ele deve fazer final e retorna _False_ se ele não deve fazer final

exemplo:
```python
def funcao():
    # algum processamento
    return True
    # outro processamento
    return False
    ```