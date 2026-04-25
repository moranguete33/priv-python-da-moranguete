import customtkinter as ctk
import random

# --- LÓGICA ---
lista_alunos = []

def registrar_aluno():
    nome = entrada_nome.get()
    
    if nome != "":
        lista_alunos.append(nome)
        
        texto_exibicao = "\n".join([f"💖 {aluno} 💖" for aluno in lista_alunos])
        
        rotulo_lista.configure(
            text=f"🎀 Lista de Alunos 🎀\n{texto_exibicao}"
        )
        
        entrada_nome.delete(0, 'end')


# --- ✨ EFEITOS VISUAIS ---
def spawn_glitter():
    x = random.randint(0, 600)
    y = random.randint(0, 650)
    
    emoji = random.choice(["✨", "💖", "🌸"])
    
    label = ctk.CTkLabel(janela, text=emoji, text_color="#F0CEE7")
    label.place(x=x, y=y)
    
    janela.after(1200, lambda: label.destroy())

def spawn_coracao():
    x = random.randint(50, 650)
    y = 750
    
    heart = ctk.CTkLabel(janela, text="💖", text_color="#C788A7", font=("Arial", 20))
    heart.place(x=x, y=y)
    
    subir_coracao(heart, y)

def subir_coracao(label, y):
    if y > -20:
        label.place(y=y-3)
        janela.after(50, lambda: subir_coracao(label, y-3))
    else:
        label.destroy()

def animar():
    spawn_glitter()
    if random.random() < 0.7:
        spawn_coracao()
    janela.after(200, animar)


# --- INTERFACE ---
ctk.set_appearance_mode("light")

janela = ctk.CTk()
janela.title(" FREQUENCIA ESCOLAR ")

# 💅 JANELA MAIOR
janela.geometry("700x750")
janela.configure(fg_color="#FFF0F5")

# 🌸 FRAME CENTRAL (glass aesthetic)
frame = ctk.CTkFrame(
    janela,
    fg_color="#FFFFFF",
    corner_radius=40,
    border_color="#FFB6C1",
    border_width=2
)
frame.place(relx=0.5, rely=0.5, anchor="center")

# 🎀 TÍTULO
titulo = ctk.CTkLabel(
    frame,
    text="🎀✨ Frequência dos Alunos ✨🎀",
    font=("Georgia", 28, "bold"),
    text_color="#FF69B4"
)
titulo.pack(pady=20)

# 💌 INPUT
entrada_nome = ctk.CTkEntry(
    frame,
    placeholder_text="Digite o nome do aluno... 💖",
    width=300,
    height=40,
    fg_color="white",
    border_color="#FFB6C1",
    text_color="#4B004B",
    corner_radius=15
)
entrada_nome.pack(pady=15)

# 💖 BOTÃO
botao = ctk.CTkButton(
    frame,
    text="✨ Registrar ✨",
    command=registrar_aluno,
    fg_color="#FFB6C1",
    hover_color="#FF69B4",
    text_color="white",
    corner_radius=30,
    height=40
)
botao.pack(pady=15)

# 🌸 LISTA
rotulo_lista = ctk.CTkLabel(
    frame,
    text="🎀 Nenhum aluno registrado ainda 🎀",
    justify="left",
    text_color="#C71585",
    font=("Georgia", 15)
)
rotulo_lista.pack(pady=20)

# ✨ iniciar animação
animar()

janela.mainloop()