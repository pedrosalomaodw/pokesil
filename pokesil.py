import openai
import os

LOG_FILE = "feedback_log.txt"
API_KEY_FILE = "api_key.txt"

def load_api_key():
    if os.path.exists(API_KEY_FILE):
        with open(API_KEY_FILE, "r") as file:
            return file.read().strip()
    else:
        return None

def save_api_key(api_key):
    with open(API_KEY_FILE, "w") as file:
        file.write(api_key)

def load_feedback_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            return file.readlines()
    else:
        return []

def save_feedback_log(log_entries):
    with open(LOG_FILE, "w") as file:
        file.writelines(log_entries)

def get_response(user_input, engine):
    api_key = load_api_key()
    if not api_key:
        raise ValueError("Chave de API não encontrada. Execute o main.py para inserir a chave de API.")

    openai.api_key = api_key
    # Implemente o código para chamar a API do OpenAI e obter a resposta
    return "Esta é uma resposta de exemplo do ELI."

def provide_feedback(response, feedback):
    api_key = load_api_key()
    if not api_key:
        raise ValueError("Chave de API não encontrada. Execute o main.py para inserir a chave de API.")

    openai.api_key = api_key
    if feedback in ['bom', 'ruim', 'neutro', 'excelente']:
        # Envie feedback para a API do OpenAI
        openai.Feedback.create(model='text-davinci-003', data=response, label=feedback)
    else:
        raise ValueError("Feedback inválido. Use 'bom', 'ruim', 'neutro' ou 'excelente'.")

def main():
    print("""
        ####################################################################
        ##                                                                ##
        ##           EEEEEEEEE     L             IIIIIII                  ##
        ##           E             L                I                     ##
        ##           E             L                I                     ##
        ##           EEEEEEE       L                I                     ##
        ##           E             L                I                     ##
        ##           E             L                I                     ##
        ##           EEEEEEEEE     LLLLLLLLLL    IIIIIII                  ##
        ##                                                                ##
        ####################################################################
    """)
    print ("""\033[1;32;40m   Bem-vindo ao ELI - Sua Assistente de Inteligência Artificial

        GitHub: https://github.com/AloneUsableUser/Eli
    """)
    print("\033[0;37;40m")
    print("Para enviar feedback por e-mail, envie para: codelong@proton.me")
    feedback_log = load_feedback_log()

    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            print("Até logo!")
            break

        try:
            response = get_response(user_input, engine="text-davinci-003")
            print("ELI:", response)
            
            # Solicitar feedback do usuário
            feedback = input("O que você achou da resposta? (bom/ruim/neutro/excelente): ").lower()
            if feedback in ['bom', 'ruim', 'neutro', 'excelente']:
                provide_feedback(response, feedback)
                feedback_log.append(f"{user_input}\t{response}\t{feedback}\n")
            else:
                print("Feedback inválido. Use 'bom', 'ruim', 'neutro' ou 'excelente'.")
        except Exception as e:
            print("Erro ao obter resposta:", e)

    save_feedback_log(feedback_log)

if __name__ == "__main__":
    main()
