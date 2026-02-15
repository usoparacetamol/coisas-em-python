import yt_dlp
import os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
Arquivos_baixados = os.path.join(DIRETORIO_ATUAL, 'downloads')

def baixar_midia(url):
    if not os.path.exists(Arquivos_baixados):
        os.makedirs(Arquivos_baixados)
        print(f"📁 Pasta criada em: {Arquivos_baixados}")

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(Arquivos_baixados, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"\n✅ Salvo com sucesso na pasta: {Arquivos_baixados}")
    except Exception as e:
        print(f"\n❌ Erro: {e}")

if __name__ == "__main__":
    link = input("URL da rede social: ")
    baixar_midia(link)
