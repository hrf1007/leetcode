
class Person:
    def __init__(self, name):
        
        self.name = name
        
        self.blood = 100
   
    def installBullet(self, clip, bullet):
        
        clip.saveBullets(bullet)
   
    def installClip(self, gun, clip):
        
        gun.mountingClip(clip)

        
        def takeGun(self, gun):
            self.gun = gun
        
        def fire(self, enemy):
           
            self.gun.shoot(enemy)

        def __str__(self):
            return self.name + "剩余血量为：" + str(self.blood)

        
        def loseBlood(self, damage):
            self.blood -= damage


class Clip:
    def __init__(self, capacity):
       
        self.capacity = capacity
        
        self.currentList = []
    
    def saveBullets(self, bullet):
        
        if len(self.currentList) < self.capacity:
            self.currentList.append(bullet)
    def __str__(self):
        return "弹夹当前的子弹数量为：" + str(len(self.currentList)) + "/" +str(self.capacity)
    
    def shotBullet(self):
        
        if len(self.currentList) > 0:
            bullet = self.currentList[-1]
            self.currentList.pop()
            return bullet
        else:
            return None

class Bullet:
    
    class Bullet:
        def __init__(self, damage):
           
            self.damage = damage

       
        def hurt(self, enemy):
           
            enemy.loseBlood(self.damage)


soldier = Person("老王")

clip = Clip(20)
print(clip)

i = 0
while i<5:
    
    bullet = Bullet()
    
    soldier.installBullet(clip, bullet)
    i += 1

print(clip)


class Gun:
    def __init__(self):
        
        self.clip = None
    def __str__(self):
        if self.clip:
            return "枪当前有弹夹"
        else:
            return "枪没有弹夹"
   
    def mountingClip(self, clip):
        if not self.clip:
            self.clip = clip
        
        def shoot(self, enemy):
            bullet = self.clip.shotBullet()
            if bullet:
                bullet.hurt(enemy)
            else:
                print("没有子弹了，放了空枪...")



gun = Gun()
print(gun)

soldier.installClip(gun, clip)
print(gun)




enemy = Person("敌人")
print(enemy)

soldier.takeGun(gun)

soldier.fire(enemy)
print(clip)
print(enemy)
soldier.fire(enemy)
print(clip)
print(enemy)