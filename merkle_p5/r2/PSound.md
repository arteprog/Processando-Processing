
#### Nome
### PSound

#### Exemplos

```pde
PSound soundA; 
 
void setup() { 
  soundA = loadSound("clong.wav"); 
  soundA.loop(); 
  framerate(24); 
} 
 
void draw() { 
  println(soundA.time()); 
} 
 

```

#### Descrição
Classe para armazenar e tocar sons no formato .wav.
Métodos
[play()](PSound_play_)
Tocar o som uma vez
[loop()](PSound_loop_)
Tocar o som continuamente
[noLoop()](PSound_noLoop_)
Parar de tocar o som continuamente
[pause()](PSound_pause_)
Pausar a reprodução do som em playback
[stop()](PSound_stop_)
Parar a reprodução do som em playback
[volume()](PSound_volume_)
Ajusta o volume da reprodução do som em playback
[duration()](PSound_duration_)
Retorna a duração do som em segundos
[time()](PSound_time_)
Retorna o momento atual de reprodução do som em playback
Construtores
```pde
PSound(file)

```
Parâmetros
file
String: nome do arquivo de som a carregar

#### Utilização

	
Web & Applicações
