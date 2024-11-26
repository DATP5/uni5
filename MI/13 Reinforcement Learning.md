![[Pasted image 20241125102448.png]]

## Ex 1
![[Pasted image 20241125101906.png]]
![[Pasted image 20241125101922.png]]


![[Pasted image 20241125101933.png]]
1. $Q((1,2), north)\leftarrow(1-0.9)\cdot0+0.9(-1+\gamma\cdot0)=-0.9$
2. $Q((1,1), east)\leftarrow(1-0.9)\cdot0+0.9(+5+\gamma\cdot0)=4.5$
3. $Q((2,1), east)\leftarrow(1-0.9)\cdot0+0.9(-2+\gamma\cdot0)=-1.8$
4. $Q((2,2), east)\leftarrow(1-0.9)\cdot0+0.9(+2+\gamma\cdot0)=1.8$

![[Pasted image 20241125101942.png]]
Not north, anything else

## Ex 2
![[Pasted image 20241125103325.png]]
![[Pasted image 20241125103334.png]]

|     | s1  | s2  |
| --- | --- | --- |
| a1  | 1   | 0   |
| a2  | 0   | 1   |

![[Pasted image 20241125103345.png]]

| R(s,a) | s1  | s2  |
| ------ | --- | --- |
| a1     | +1  | +7  |
| a2     | -2  | +2  |

![[Pasted image 20241125103352.png]]

| $Q_0$ | s1  | s2  |
| ----- | --- | --- |
| a1    | 0   | 0   |
| a2    | 0   | 0   |
$Q(s1, a1) \leftarrow (1-0.9)0+0.9(1+\gamma\cdot0)=0.9$

| $Q_1$ | s1  | s2  |
| ----- | --- | --- |
| a1    | 0.9 | 0   |
| a2    | 0   | 0   |
$Q(s1, a1) \leftarrow (1-0.9)0.9+0.9(1+0.95\cdot0.9)=1.76$

| $Q_2$ | s1   | s2  |
| ----- | ---- | --- |
| a1    | 1.76 | 0   |
| a2    | 0    | 0   |
This keeps happening, oh my gawd, we need to explore since s2 is awesome

![[Pasted image 20241125103359.png]]

| $Q_0$ | s1  | s2  |
| ----- | --- | --- |
| a1    | 0   | 0   |
| a2    | 0   | 0   |
$Q(s1, a2) \leftarrow (1-0.9)0+0.9(-2+\gamma\cdot0)=-1.8$

| $Q_1$ | s1   | s2  |
| ----- | ---- | --- |
| a1    | 0    | 0   |
| a2    | -1.8 | 0   |
$Q(s2, a1) \leftarrow (1-0.9)0+0.9(7+\gamma\cdot0)=6.3$

| $Q_2$ | s1   | s2  |
| ----- | ---- | --- |
| a1    | 0    | 6.3 |
| a2    | -1.8 | 0   |
$Q(s1, a1) \leftarrow (1-0.9)0+0.9(1+\gamma\cdot0)=0.9$

| $Q_2$ | s1   | s2  |
| ----- | ---- | --- |
| a1    | 0.9  | 6.3 |
| a2    | -1.8 | 0   |
$Q(s1, a2) \leftarrow (1-0.9)\cdot-1.8+0.9(-2+0.95\cdot6.3)=3.4$ (tror markus og emil, markus ville ikke have alt ansvar)

| $Q_2$ | s1  | s2  |
| ----- | --- | --- |
| a1    | 0.9 | 6.3 |
| a2    | 3.4 | 0   |

![[Pasted image 20241125105224.png]]

| R(s,a) | s1  | s2  |
| ------ | --- | --- |
| a1     | +1  | +7  |
| a2     | -2  | +2  |

The good cycle is back and fourth, and then we goooo:

$V^{*}(s_{1})=max(1+0.95\cdot V^{*}(s_{1}), -2+0.95\cdot V^{*}(s_{2}))=-2+0.95\cdot V^{*}(s_{2})$
$V^{*}(s_{2})=max(7+0.95\cdot V^{*}(s_{1}), 2+0.95\cdot V^{*}(s_{2}))=7+0.95\cdot V^{*}(s_{1})$

$V^{*}(s_{1})=-2+0.95\cdot (7+0.95\cdot V^{*}(s_{1}))$
$\Leftrightarrow V^{*}(s_{1})=47.69$

$V^{*}(s_{2})=7+0.95\cdot (-2+0.95\cdot V^{*}(s_{2}))$
$\Leftrightarrow V^{*}(s_{2})=52.31$


![[Pasted image 20241125111607.png]]

$Q^{*}(s,a)=R(s,a)+\gamma\cdot V^{*}(s')$

| $Q^*(s,a)$ | s1                        | s2                       |
| ---------- | ------------------------- | ------------------------ |
| a1         | $1+0.95\cdot47.69=46.31$  | $7+0.95\cdot47.69=52.30$ |
| a2         | $-2+0.95\cdot52.31=47.69$ | $2+0.95\cdot52.31=51.69$ |

## Ex 3
![[Pasted image 20241125111949.png]]
![[Pasted image 20241125112005.png]]
Yes, slide 21 states Q-learning is guaranteed to converge under certain circumstances, and from there, a policy may be extracted. This all works without prior knowledge of reward function or transition probabilities

![[Pasted image 20241125112134.png]]
False, see exercise 2.iii