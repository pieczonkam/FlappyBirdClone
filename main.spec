# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             pathex=['D:\\MyGames\\Flappy Bird'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [('fonts\\The Bomb Sound.ttf', 'D:\\MyGames\\Flappy Bird\\fonts\\The Bomb Sound.ttf', 'DATA'),
            ('Sounds\\sfx_die.wav', 'D:\\MyGames\\Flappy Bird\\Sounds\\sfx_die.wav', 'DATA'),
            ('Sounds\\sfx_hit.wav', 'D:\\MyGames\\Flappy Bird\\Sounds\\sfx_hit.wav', 'DATA'),
            ('Sounds\\sfx_point.wav', 'D:\\MyGames\\Flappy Bird\\Sounds\\sfx_point.wav', 'DATA'),
            ('Sounds\\sfx_wing.wav', 'D:\\MyGames\\Flappy Bird\\Sounds\\sfx_wing.wav', 'DATA'),
            ('Sounds\\sfx_swooshing.wav', 'D:\\MyGames\\Flappy Bird\\Sounds\\sfx_swooshing.wav', 'DATA'),
            ('Graphics\\bird_blue.png', 'D:\\MyGames\\Flappy Bird\\Graphics\\bird_blue.png', 'DATA'),
            ('Graphics\\bird_green.png', 'D:\\MyGames\\Flappy Bird\\Graphics\\bird_green.png', 'DATA'),
            ('Graphics\\bird_red.png', 'D:\\MyGames\\Flappy Bird\\Graphics\\bird_red.png', 'DATA'),
            ('Graphics\\bird_yellow.png', 'D:\\MyGames\\Flappy Bird\\Graphics\\bird_yellow.png', 'DATA'),
            ('Graphics\\ground.png', 'D:\\MyGames\\Flappy Bird\\Graphics\\ground.png', 'DATA'),
            ('Graphics\\pipe.png', 'D:\\MyGames\\Flappy Bird\\Graphics\\pipe.png', 'DATA'),
            ('Graphics\\pipe_upside_down.png', 'D:\\MyGames\\Flappy Bird\\Graphics\\pipe_upside_down.png', 'DATA'),
            ('Graphics\\sky.png', 'D:\\MyGames\\Flappy Bird\\Graphics\\sky.png', 'DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Flappy Bird',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='D:\\MyGames\\Flappy Bird\\applogo.ico')
