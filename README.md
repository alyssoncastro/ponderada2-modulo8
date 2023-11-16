# Documentação da Ponderada 3 - Engenharia da Computação.

### Autor: Alysson C. C. Cordeiro.

Este projeto permite simular um TurtleBot3 no ambiente Gazebo e realizar navegação utilizando o pacote de navegação nav2.

O projeto é feito por **turtlebot3_navigation2**, que é o  pacote que contém todas configurações da navegação para o TurtleBot3. Tem **turtlebot3_gazebo** que é o pacote para simulação do  TurtleBot3. E **meu_pacote** que é o paconte que personalizei contendo os nós.

## REQUISITO:

Primeiramente, não esqueça antes de tudo instalar o ROS 2 no seu ambiente. A documentação você pode encontrar aqui: [Ros Documentation](https://docs.ros.org/)

1. Em seguinda, execute o comando embaixo para iniciar o ROS2:

```python
ros-start
```
Aparecerá um robozinho ao lado.

2. Abre o terminal e navegue até o diretório **meu_pacote**
```python
cd mapa/ros2_workspace/src/meu_pacote
```

3. Execute o comando para construção e compilação:

```python
colcon build
```
4. Agora execute o comando **source** para colocar o pacote ao seu ambiente:
```python
# Estou usando zsh. Mas troque bash se caso estiver usando.
source install/setup.zsh
```

5. Para executar o projeto, execute **ros2 launch**, mais o pacote, mais o arquivo do script:

```python
ros2 launch meu_pacote test_launch.py
```

## OBSERVAÇÕES E FALHAS:

Ambiente de início mostrava sucesso, contudo foi denotado erros constantemente de aparições e falhas no Rviz ao tentar compilar meu pacote. Novamente o mapa não tinha aparecido, sumiu. Mesmo já configurado o arquivo **burger.yaml** para **"robot_model_type: "nav2_amcl::DifferentialMotionModel"**. 
Veja a imagem a seguir do setup burger.yaml:

link da imagem: https://drive.google.com/file/d/1E-D79ARgFwla_QxDMLm0V2z0Og2OGfVX/view?usp=sharing

O script funciona. Contudo, o ambiente de execução, não. 
Veja o vídeo a seguir de como foi executado e as também suas falhas. 

link: https://drive.google.com/file/d/113a1O6OuxZSq9dNeM8NsF2IJ1s-rqSSW/view?usp=sharing

Houve várias tentativas. Contudo, sem sucesso. O Rivz abre ao executar o comando, mas automaticamente fecha por conta própria sem nem aparecer o mapa.

## Nota:
Em esclarimento para o Professor Nicola, eu peço desculpa por não conseguir desvendar esse erro e por um ótimo padrão de qualidade da atividade. Entretanto, qualquer dúvida e feedbacks, eu estarei disposto a ouvir.