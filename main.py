import sys
from roles import RolesPreset
from chat_service import ChatService
from config import settings
def choose_role() -> RolesPreset:
    print("Elegí un rol inicial:")
    print("1) Profesor 2) Traductor 3) Programador 4) Asistente")
    sel = input("> ").strip()
    mapping = {
        "1": RolesPreset.PROFESOR,
        "2": RolesPreset.TRADUCTOR,
        "3": RolesPreset.PROGRAMADOR,
        "4": RolesPreset.ASISTENTE,
    }
    return mapping.get(sel, RolesPreset.ASISTENTE)
def print_help():
    print("\nComandos:")
    print(":rol profesor|traductor|programador|asistente -> cambia el rol")
    print(":reset -> limpia la memoria")
    print(":salir -> termina\n")

def main():
    print(f"🤖 {settings.system_name}")
    role = choose_role()
    chat = ChatService(role=role)
    print_help()
    while True:
        try:
            user = input("🧑 Vos: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Chau!")
            break
        if not user:
            continue
        # Comandos
        if user.lower() in (":salir", "salir", "exit", "quit"):
            print("👋 ¡Chau!")
            break
        if user.lower() == ":reset":
            chat.reset()
            print("🧼 Memoria borrada.")
            continue
        if user.lower().startswith(":rol"):
            _, *rest = user.split()
            new_role = (rest[0] if rest else "").lower()
            mapping = {
            "profesor": RolesPreset.PROFESOR,
            "traductor": RolesPreset.TRADUCTOR,
            "programador": RolesPreset.PROGRAMADOR,
            "asistente": RolesPreset.ASISTENTE,
            }
            if new_role in mapping:
                chat.set_role(mapping[new_role])
                print(f"🎭 Rol cambiado a: {new_role}")
            else:
                print("⚠️ Rol inválido. Opciones: profesor, traductor, programador, asistente.")
            continue
        if user.lower() == ":help":
            print_help()
            continue
        # Pregunta normal
        try:
            answer = chat.ask(user)
            print("🤖 Bot:", answer)
        except Exception as e:
            print("❌ Error manejado:", e)
if __name__ == "__main__":
    main()
