"""
Aplicação Desktop de Lista de Tarefas (Tkinter)
Desafio 3 - Imersão Alura com IA & Google Antigravity
Interface gráfica nativa em Python com distinção visual de tarefas concluídas.
"""
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

ARQUIVO_DADOS = os.path.join(os.path.dirname(__file__), "tarefas.json")

class TodoAppTkinter:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Minhas Tarefas • Google Antigravity")
        self.root.geometry("520x620")
        self.root.minsize(440, 500)
        self.root.configure(bg="#f1f5f9")

        self.tarefas = self.carregar_tarefas()

        self.criar_interface()
        self.atualizar_lista()

    def carregar_tarefas(self):
        if os.path.exists(ARQUIVO_DADOS):
            try:
                with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def salvar_tarefas(self):
        try:
            with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
                json.dump(self.tarefas, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar as tarefas: {e}")

    def criar_interface(self):
        # Cabeçalho
        header_frame = tk.Frame(self.root, bg="#f1f5f9")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))

        badge = tk.Label(
            header_frame, 
            text="DESAFIO 3 • GOOGLE ANTIGRAVITY", 
            font=("Segoe UI", 9, "bold"), 
            fg="#4f46e5", 
            bg="#eef2ff",
            padx=10, 
            pady=4
        )
        badge.pack(anchor="center", pady=(0, 6))

        titulo = tk.Label(
            header_frame, 
            text="Minhas Tarefas", 
            font=("Segoe UI", 18, "bold"), 
            fg="#0f172a", 
            bg="#f1f5f9"
        )
        titulo.pack(anchor="center")

        subtitulo = tk.Label(
            header_frame, 
            text="Interface visual em Python Desktop", 
            font=("Segoe UI", 10), 
            fg="#64748b", 
            bg="#f1f5f9"
        )
        subtitulo.pack(anchor="center")

        # Campo de Entrada e Botão Adicionar
        input_frame = tk.Frame(self.root, bg="#f1f5f9")
        input_frame.pack(fill="x", padx=20, pady=10)

        self.entry_tarefa = ttk.Entry(input_frame, font=("Segoe UI", 11))
        self.entry_tarefa.pack(side="left", fill="x", expand=True, ipady=6, padx=(0, 8))
        self.entry_tarefa.bind("<Return>", lambda e: self.adicionar_tarefa())

        btn_adicionar = tk.Button(
            input_frame,
            text="+ Adicionar",
            font=("Segoe UI", 10, "bold"),
            bg="#4f46e5",
            fg="white",
            activebackground="#4338ca",
            activeforeground="white",
            relief="flat",
            padx=14,
            pady=6,
            cursor="hand2",
            command=self.adicionar_tarefa
        )
        btn_adicionar.pack(side="right")

        # Barra de Estatísticas
        self.lbl_stats = tk.Label(
            self.root,
            text="0 tarefas | 0 concluídas | 0 pendentes",
            font=("Segoe UI", 9),
            fg="#64748b",
            bg="#f1f5f9"
        )
        self.lbl_stats.pack(fill="x", padx=20, pady=(0, 6))

        # Container da Lista com Scrollbar
        list_container = tk.Frame(self.root, bg="white", bd=1, relief="solid")
        list_container.pack(fill="both", expand=True, padx=20, pady=10)

        self.canvas = tk.Canvas(list_container, bg="white", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(list_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="white")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.itemconfig(self.canvas_window, width=e.width)
        )

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def adicionar_tarefa(self):
        texto = self.entry_tarefa.get().strip()
        if not texto:
            messagebox.showwarning("Atenção", "Por favor, digite o nome da tarefa.")
            return

        nova = {
            "id": len(self.tarefas) + 1,
            "texto": texto,
            "concluida": False
        }
        self.tarefas.append(nova)
        self.salvar_tarefas()
        self.entry_tarefa.delete(0, tk.END)
        self.atualizar_lista()

    def alternar_conclusao(self, indice):
        self.tarefas[indice]["concluida"] = not self.tarefas[indice]["concluida"]
        self.salvar_tarefas()
        self.atualizar_lista()

    def remover_tarefa(self, indice):
        del self.tarefas[indice]
        self.salvar_tarefas()
        self.atualizar_lista()

    def atualizar_lista(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        total = len(self.tarefas)
        concluidas = sum(1 for t in self.tarefas if t.get("concluida"))
        pendentes = total - concluidas
        self.lbl_stats.config(text=f"Total: {total} | Concluídas: {concluidas} | Pendentes: {pendentes}")

        if not self.tarefas:
            lbl_vazio = tk.Label(
                self.scrollable_frame,
                text="📝 Nenhuma tarefa cadastrada.\nAdicione sua primeira atividade acima!",
                font=("Segoe UI", 11),
                fg="#94a3b8",
                bg="white",
                pady=40
            )
            lbl_vazio.pack(fill="x", expand=True)
            return

        for idx, tarefa in enumerate(self.tarefas):
            item_frame = tk.Frame(
                self.scrollable_frame, 
                bg="#f8fafc" if not tarefa["concluida"] else "#f1f5f9",
                bd=1, 
                relief="solid"
            )
            item_frame.pack(fill="x", padx=10, pady=4, ipady=4)

            # Botão de Checkbox visual
            check_text = "☑" if tarefa["concluida"] else "☐"
            btn_check = tk.Button(
                item_frame,
                text=check_text,
                font=("Segoe UI", 12, "bold"),
                fg="#10b981" if tarefa["concluida"] else "#94a3b8",
                bg=item_frame["bg"],
                relief="flat",
                bd=0,
                cursor="hand2",
                command=lambda i=idx: self.alternar_conclusao(i)
            )
            btn_check.pack(side="left", padx=8)

            # Texto da Tarefa (com distinção visual para concluída)
            texto_formatado = f"~ {tarefa['texto']} ~" if tarefa["concluida"] else tarefa["texto"]
            cor_texto = "#94a3b8" if tarefa["concluida"] else "#0f172a"
            fonte = ("Segoe UI", 10, "overstrike") if tarefa["concluida"] else ("Segoe UI", 10)

            lbl_texto = tk.Label(
                item_frame,
                text=texto_formatado,
                font=fonte,
                fg=cor_texto,
                bg=item_frame["bg"],
                anchor="w",
                cursor="hand2"
            )
            lbl_texto.pack(side="left", fill="x", expand=True, padx=4)
            lbl_texto.bind("<Button-1>", lambda e, i=idx: self.alternar_conclusao(i))

            if tarefa["concluida"]:
                lbl_badge = tk.Label(
                    item_frame,
                    text="Concluída",
                    font=("Segoe UI", 8, "bold"),
                    fg="#10b981",
                    bg="#ecfdf5",
                    padx=6,
                    pady=2
                )
                lbl_badge.pack(side="left", padx=6)

            # Botão de Remover (Lixeira)
            btn_delete = tk.Button(
                item_frame,
                text="✕",
                font=("Segoe UI", 10, "bold"),
                fg="#ef4444",
                bg=item_frame["bg"],
                relief="flat",
                bd=0,
                cursor="hand2",
                command=lambda i=idx: self.remover_tarefa(i)
            )
            btn_delete.pack(side="right", padx=8)

def main():
    root = tk.Tk()
    app = TodoAppTkinter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
