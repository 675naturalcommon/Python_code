cities = {
    'santiago': {
        'country': 'chile',
        'population': 6000000,
        'nearby_mountains': ['mount elbrus', 'kilimanjaro', 'everest'],
        'nearby_rivers': ['seine', 'ile de france', 'rhone'],
        'nearby_cities': ['madrid', 'barcelona', 'valencia'],
    },
    'paris': {
        'country': 'france',
        'population': 22000000,
        'nearby_mountains': ['mount eiffel', 'pyrenees', 'columbier'],
        'nearby_rivers': ['seine', 'marne', 'ourcq'],  # 修正为巴黎附近的河流
        'nearby_cities': ['london', 'rome', 'lyon'],
    }
}
# 打印出每个城市的基本信息
for city, info in cities.items():
    print(f"{city.title()} has a population of {info['population']} and is located in {info['nearby_mountains']}")
    print(f"It is connected to {info['nearby_rivers']} and has a coastline in {info['nearby_cities']}")  # 修正为“附近” -> “连接”
    print()  # 空行            