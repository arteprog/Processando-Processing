<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### PSound
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>
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
<img height="25" src="../images/1pix.gif" width="1"/>
<img height="25" src="../images/1pix.gif" width="1"/>
Construtores
```pde
PSound(<font color="#996600">file</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
file
String: nome do arquivo de som a carregar
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>
