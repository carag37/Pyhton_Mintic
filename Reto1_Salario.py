salario_base, horas_extra, bonificaciones = input().split()

salario_base = float(salario_base)
horas_extra = int(horas_extra)
bonificaciones = int(bonificaciones)

valor_extra = (salario_base / 192) * 1.25 * horas_extra
valor_bonificacion = 0.05 * salario_base * bonificaciones
salario_total = salario_base + valor_extra + valor_bonificacion
salario_pagar = salario_total - 0.035 * salario_total - 0.04 * salario_total - 0.01 * salario_total

print(round(salario_pagar, 1))


