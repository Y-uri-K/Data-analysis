INSERT INTO "levels" (difficulty)
VALUES 
    ('easy'),
    ('normal'),
    ('hard'),
    ('insane'),
    ('impossible');

INSERT INTO "actions" (action_name, action_type)
VALUES 
    ('run', 'movement'),
    ('collect coin', 'collectible'),
    ('open chest', 'collectible'),
    ('upgrade weapon', 'upgrade'),
    ('shoot', 'combat'),
    ('boss die', 'finish'),
    ('heal', 'support');

