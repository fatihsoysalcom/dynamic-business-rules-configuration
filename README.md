# Dynamic Business Rules Configuration

This example demonstrates how software can achieve rapid adaptation to changing business needs by externalizing business rules into a simple configuration file. It simulates an order processing system where discount and shipping rules are defined in `config.json`. By modifying this file, the software's behavior changes instantly without requiring any code modifications or redeployment, illustrating agility and responsiveness to market demands.

## Language

`python`

## How to Run

1. Save the code as `main.py` in an empty directory.
2. Run `python main.py` once to generate the initial `config.json` and see the default behavior.
3. Edit `config.json` to change business rules (e.g., adjust discount percentages or free shipping thresholds).
4. Run `python main.py` again to observe the immediate effect of the updated rules.

## Original Article

This example accompanies the Turkish article: [Yazılım İş Dünyasından Hızlı Olmalı: Dijital Çağda Rekabet Avantajı](https://fatihsoysal.com/blog/yazilim-is-dunyasindan-hizli-olmali-dijital-cagda-rekabet-avantaji/).

## License

MIT — see [LICENSE](LICENSE).
