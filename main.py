import psycopg2
import matplotlib.pyplot as plt

username = 'Bilovodskiy_I'
password = '1234'
database = 'laptops'
host = 'localhost'
port = '5432'

query_1 = '''
CREATE VIEW GPU_NB as
select gpu_series,count(name) from laptop 
inner join gpu on laptop.gpu_id=gpu.gpu_id 
group by gpu_series	
'''
query_2 = '''
CREATE VIEW CPU_NB as
select cpu_series,count(name) from laptop 
inner join cpu on laptop.cpu_id=cpu.cpu_id 
group by cpu_series

'''

query_3 = '''
CREATE VIEW OS_NB as
select os_name,count(name) from laptop 
inner join os on laptop.os_id=os.os_id 
group by os_name
'''
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
with conn:
    cur = conn.cursor()

    cur.execute('DROP VIEW IF EXISTS GPU_NB')

    cur.execute(query_1)
    cur.execute('select * from GPU_NB')
    eff = []
    eff_count = []

    for row in cur:
        eff.append(row[0])
        eff_count.append(row[1])

    cur.execute('DROP VIEW IF EXISTS CPU_NB')

    cur.execute(query_2)
    cur.execute('select * from CPU_NB')
    mnf = []
    mnf_count = []

    for row in cur:
        mnf.append(row[0])
        mnf_count.append(row[1])

    cur.execute('DROP VIEW IF EXISTS OS_NB')

    cur.execute(query_3)
    cur.execute('select * from OS_NB')
    os = []
    os_count = []

    for row in cur:
        os.append(row[0])
        os_count.append(row[1])

    fig, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)

    # bar
    bar_ax.set_title('К-сть ноутбуків на певній відеокарті')
    bar_ax.set_xlabel('Відеокарта')
    bar_ax.set_ylabel('К-сть')
    bar = bar_ax.bar(eff, eff_count)
    bar_ax.set_xticks(range(len(eff)))
    bar_ax.set_xticklabels(eff, rotation=30)

     # pie
    pie_ax.pie(os_count, labels=os, autopct='%1.1f%%')
    pie_ax.set_title('Відношення поставлених операційних систем')

     # graph
    graph_ax.plot(mnf, mnf_count, marker='o')
    graph_ax.set_xlabel('Процессори')
    graph_ax.set_ylabel('Кількість')
    graph_ax.set_title('Графік залежності к-сть ноутбуків на процесорі')
    graph_ax.set_xticklabels(mnf, rotation=30)
    for chn, count in zip(mnf, mnf_count):
        graph_ax.annotate(count, xy=(chn, count), xytext=(7, 2), textcoords='offset points')

plt.get_current_fig_manager().resize(1400, 600)
plt.show()