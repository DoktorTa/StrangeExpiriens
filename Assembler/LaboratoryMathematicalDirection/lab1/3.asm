.486
.MODEL Flat, StdCall ; StdCall - мантра
include \masm32\include\msvcrt.inc
includelib \masm32\lib\msvcrt.lib

.data
Format db '%d', 0
A dd 10
B dd 20
SEVEN_TEEN dd 17
.CODE
;Напишите программу, которая находит остаток от деления на 17 произведения двух
;беззнаковых 4-байтных чисел, заданных в переменных a и b.
main:
	; eax = 1, тоесть число a = 10
	; ebx = 2, тоесть число b = 20
	mov eax, A
	mov ebx, B
	
	; eax = eax * ebx
	mul ebx
	
	; ebx = 17, тоесть третье число 17
	mov ebx, SEVEN_TEEN
	
	; edx / ebx Результат деления в eal, остаток в edx
	div ebx
	
	; Вывод результата на экран
	invoke crt_printf, addr Format, edx
	
	; И это мантра (пока что)
	ret
end main