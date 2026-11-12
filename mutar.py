

from pathlib import Path
import subprocess
import sys
import tempfile
import shutil

pasta = Path(__file__).parent
arquivo = pasta / "desconto.py"
arquivo_testes = pasta / "test_desconto.py"

codigo_original = arquivo.read_text(encoding="utf-8")
testes_originais = arquivo_testes.read_text(encoding="utf-8")

mutacoes = mutacoes = [
    {
        "nome": "Mutação 1: > para >=",
        "original": "percentual > 100",
        "alterado": "percentual >= 100",
    },
    {
        "nome": "Mutação 2: < para <=",
        "original": "percentual < 0",
        "alterado": "percentual <= 0",
    },
    {
        "nome": "Mutação 3: adicionar 1 ao resultado",
        "original": "return preco * (1 - percentual / 100)",
        "alterado": "return preco * (1 - percentual / 100) + 1",
    },  
    {
        "nome": "Mutação 4: alterar mensagem de erro",
        "original": "Percentual inválido.",
        "alterado": "Valor inválido.",
    
},
]

mortos = 0
sobreviventes = 0
erros = 0

try:
    for i, mutacao in enumerate(mutacoes):
        print(f"\n--- {mutacao['nome']} ---")

        codigo_mutado = codigo_original.replace(
            mutacao["original"],
            mutacao["alterado"],
            1
        )

        if codigo_mutado == codigo_original:
            print("ERRO: mutação não aplicada.")
            erros += 1
            continue

        with tempfile.TemporaryDirectory() as temporario:
            temp = Path(temporario)

            (temp / "desconto.py").write_text(
                codigo_mutado,
                encoding="utf-8"
            )

            # Altera somente o módulo importado pelos testes
            testes_mutados = testes_originais.replace(
                "from desconto import aplicar_desconto",
                "from desconto_mutado import aplicar_desconto"
            )

            (temp / "desconto_mutado.py").write_text(
                codigo_mutado,
                encoding="utf-8"
            )

            (temp / "test_desconto.py").write_text(
                testes_mutados,
                encoding="utf-8"
            )

            resultado = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pytest",
                    "-q",
                    str(temp / "test_desconto.py")
                ],
                cwd=temp,
                capture_output=True,
                text=True
            )

            saida = resultado.stdout + resultado.stderr
            print(saida)

            if resultado.returncode == 0:
                print("MUTANTE SOBREVIVEU")
                sobreviventes += 1

            elif " failed" in saida:
                print("MUTANTE MORTO")
                mortos += 1

            else:
                print("ERRO DE EXECUÇÃO")
                erros += 1

finally:
    print("\nCódigo original preservado.")

total = mortos + sobreviventes

print("\n===== RELATÓRIO FINAL =====")
print(f"Mutantes mortos: {mortos}")
print(f"Mutantes sobreviventes: {sobreviventes}")
print(f"Erros de execução: {erros}")

if total:
    print(f"Taxa de detecção: {mortos / total * 100:.1f}%")
else:
    print("Taxa indisponível.")
