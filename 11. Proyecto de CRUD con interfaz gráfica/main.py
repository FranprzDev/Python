import profesor_class as prof
import sql_functions as sql
import tkinter as tk

sql.conectar_sql()

profe = prof.Profesor('Francisco', 'Perez', 19, 5635523, 'Sistemas y Organizaciones', 3, '1K5')
profe1 = prof.Profesor('Francisco', 'Perez213', 19, 564335523, 'Sistemas y Organizaciones', 3, '1K5')
profe2 = prof.Profesor('Francis432co', 'Perezfgd', 19, 5635224523, 'Sistemas y Organizaciones', 3, '1K5')

#sql.crear_profesor(profe)
sql.crear_profesor(profe1)
sql.crear_profesor(profe2)

# ventana = tk.Tk()
# ventana.geometry('800x500')

# ventana.title('CRUD de Profesores - SQLite & Python')





# tk.mainloop()