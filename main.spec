# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\mac25\\Desktop\\Games\\Flappy Bird'],
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

a.datas += [('fonts\\The Bomb Sound.ttf', 'C:\\Users\\mac25\\Desktop\\Games\\Flappy Bird\\fonts\\The Bomb Sound.ttf', 'DATA'),
            ('Sounds\\sfx_die.wav', 'C:\\Users\\mac25\\Desktop\\Games\\Flappy Bird\\Sounds\\sfx_die.wav', 'DATA'),
            ('Sounds\\sfx_hit.wav', 'C:\\Users\\mac25\\Desktop\\Games\\Flappy Bird\\Sounds\\sfx_hit.wav', 'DATA'),
            ('Sounds\\sfx_point.wav', 'C:\\Users\\mac25\\Desktop\\Games\\Flappy Bird\\Sounds\\sfx_point.wav', 'DATA'),
            ('Sounds\\sfx_wing.wav', 'C:\\Users\\mac25\\Desktop\\Games\\Flappy Bird\\Sounds\\sfx_wing.wav', 'DATA'),
            ('Sounds\\sfx_swooshing.wav', 'C:\\Users\\mac25\\Desktop\\Games\\Flappy Bird\\Sounds\\sfx_swooshing.wav', 'DATA'),
            ('Graphics\\bird_blue.png', 'C:\\Users\\mac25\\Desktop\\Games\\Flappy Bird\\Graphics\\bird_blue.png', 'DATA'),
            ('Graphics\\bird_green.png', 'C:\\Users\\mac25\\Desktop\\Games\\Flappy Bird\\Graphics\\bird_green.png', 'DATA'),
            ('Graphics\\bird_red.png', 'C:\\Users\\mac25\\Desktop\\Games\\Flappy Bird\\Graphics\\bird_red.png', 'DATA'),
            ('Graphics\\bird_yellow.png', 'C:\\Users\\mac25\\Desktop\\Games\\Flappy Bird\\Graphics\\bird_yellow.png', 'DATA'),
            ('Graphics\\ground.png', 'C:\\Users\\mac25\\Desktop\\Games\\Flappy Bird\\Graphics\\ground.png', 'DATA'),
            ('Graphics\\pipe.png', 'C:\\Users\\mac25\\Desktop\\Games\\Flappy Bird\\Graphics\\pipe.png', 'DATA'),
            ('Graphics\\pipe_upside_down.png', 'C:\\Users\\mac25\\Desktop\\Games\\Flappy Bird\\Graphics\\pipe_upside_down.png', 'DATA'),
            ('Graphics\\sky.png', 'C:\\Users\\mac25\\Desktop\\Games\\Flappy Bird\\Graphics\\sky.png', 'DATA')]

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
          icon='C:\\Users\\mac25\\Desktop\\Games\\Flappy Bird\\applogo.ico')
