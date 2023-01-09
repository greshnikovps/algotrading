## Алгоритмическая торговля

В попытках заработать все деньги мира все способы хороши. Не самый простой и не самый эффективный из них - это алгоритмическая торговля биржевыми инструментами.

# Как это работает
Создаем робота, который анализирует рыночные условия (чаще всего, изменения цен тех или иных биржевых инструментов) и делает выводы на основании проведенного анализа. Если робот заметил, что в прошлом в 8 из 10 случаев после соблюдений определенных условий цена инструмента выросла, то в будущем при соблюдении тех же условий может оказаться выгодно (или не очень) вложиться в этот инструмент. 
Наша с вами задача придумывать такие паттерны, после которых цена часто изменяется в одну и ту же сторону, а задача робота - проверять эти наши гипотезы и, если мы довольнф результатом проверки, робот может начинать совершать сделки на бирже, руководствуясь нашей стратегией.

# Еще немного теории
Проанализировав рынок алготрейдинговых ботов было выяснено, что большинство из них подключается к бирже напрямую затем, чтобы избежать накладки по времени, связанные с промежуточной инстанцией "брокер". Это очень умный ход, но стоит он дороговато, поэтому мы так делать не будем, но будем понимать, что наш бот вряд ли будет конкурентоспособный на этапе торговли, но для проверки гипотез в целом подойдет.

# Ближе к делу
Итак, в итоге я написал программку которая должна запускаться, брать из конфигурационных файликов необходимую ей информацию (такую, например, как токен для подключения к бирже) и проверять различные стратегии. 

# Ладно, а как этим пользоваться?
Исползовать программу для теста своих собственных идей несложно, нужно только написать свой класс-стратегию унаследовав его от AlgorithmicAnalyzer и определив у него метод calculate_result, который будет, согласно вашей стратегии, по имеющимся ценовым данным говорить, что должен сдлать робот (купить, продать или ничего не делать).
После этого в main'е нужно название класса стратегии заменить на ваше и все готово! Как итог, скорее всего, вы получите информацию о том, что в разы прибыльнее будет, например, снимать клипы в тикток.
