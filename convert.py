import json
import os

def convert_to_netscape(json_file, netscape_file):
    """
    Converte um arquivo JSON de cookies para o formato Netscape.

    :param json_file: Caminho do arquivo de entrada
    :param netscape_file: Caminho do arquivo de saída (cookies_netscape.txt)
    """
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            cookies = json.load(f)

        with open(netscape_file, "w", encoding="utf-8") as f:
            f.write("# Netscape HTTP Cookie File\n")
            f.write("# Este arquivo pode ser importado em navegadores.\n")
            f.write("# domain\tflag\tpath\tsecure\texpiration\tname\tvalue\n")

            for cookie in cookies:
                domain = cookie.get("domain", "")
                flag = "TRUE" if domain.startswith(".") else "FALSE"
                path = cookie.get("path", "/")
                secure = "TRUE" if cookie.get("secure", False) else "FALSE"
                expiration = str(int(cookie.get("expirationDate", 0)))
                name = cookie.get("name", "")
                value = cookie.get("value", "")

                f.write(f"{domain}\t{flag}\t{path}\t{secure}\t{expiration}\t{name}\t{value}\n")
        
        print(f"✅ Conversão concluída! Arquivo salvo em: {netscape_file}")
    except Exception as e:
        print(f"❌ Erro ao converter: {e}")

if __name__ == "__main__":
    # Criar a pasta se não existir
    directory = "cookies_converter"
    os.makedirs(directory, exist_ok=True)

    # Procurar automaticamente um arquivo JSON ou TXT na pasta
    files = [f for f in os.listdir(directory) if f.endswith((".json", ".txt"))]
    
    if files:
        json_path = os.path.join(directory, files[0])  # Usa o primeiro arquivo encontrado
        netscape_path = os.path.join(directory, "cookies_netscape.txt")
        convert_to_netscape(json_path, netscape_path)
    else:
        print(f"⚠️ Nenhum arquivo JSON ou TXT encontrado na pasta {directory}. Coloque um arquivo de cookies lá e tente novamente.")
