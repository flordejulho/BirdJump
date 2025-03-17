from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def __verify_jump_over(player: Player, enemy: Enemy):
        """Verifica se o jogador saltou sobre o inimigo sem colidir e adiciona pontos."""
        if player.rect.bottom < enemy.rect.top and player.velocity < 0:  # Jogador acima e subindo
            player.score += enemy.score
            enemy.last_dmg = player.name  # Marcar que foi o jogador que gerou os pontos

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        """Verifica colisão entre jogador e inimigo, definindo game over ou pontuação."""
        if isinstance(ent1, Player) and isinstance(ent2, Enemy):
            player = ent1
            enemy = ent2
        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
            player = ent2
            enemy = ent1
        else:
            return  # Se não for uma interação válida, sai da função

        # Se o jogador saltou por cima sem tocar, ele ganha pontos
        EntityMediator.__verify_jump_over(player, enemy)

        # Se houver colisão real (lateral ou de frente), perde ponto
        if (player.rect.right >= enemy.rect.left and
                player.rect.left <= enemy.rect.right and
                player.rect.bottom >= enemy.rect.top and
                player.rect.top <= enemy.rect.bottom):
            player.health -= 1  # Game over

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        """Adiciona pontuação ao jogador se o inimigo for derrotado."""
        if enemy.last_dmg == 'Player1':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        """Verifica todas as colisões entre entidades."""
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        """Remove entidades com vida menor ou igual a 0."""
        for ent in entity_list[:]:  # Usamos [:] para evitar erro ao remover elementos enquanto iteramos
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
