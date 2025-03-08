import json
import os

def convert_to_netscape(json_file, netscape_file):
    """
    Converte um arquivo JSON de cookies para o formato Netscape.
    
    :param json_file: Caminho do arquivo de entrada (cookies.json)
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

    # Definir caminhos
    json_path = os.path.join(directory, "cookies.json")
    netscape_path = os.path.join(directory, "cookies_netscape.txt")

    # Verificar se o arquivo de entrada existe
    if os.path.exists(json_path):
        convert_to_netscape(json_path, netscape_path)
    else:
        print(f"⚠️ Arquivo {json_path} não encontrado. Coloque o cookies.json na pasta {directory} e tente novamente.")
