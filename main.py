o
    m,�b�i �                   @   s   d dl Z d dlZd dlZd dlZd dlmZmZmZ ejdd� d dlmZmZ d dlZe�  ej	Z
ejZejZejZejZejZeeeeegZdd� Ze�  dd	� Zed
� ed� ed� ed� d dlZd dlZd dlZd dlZd dl Z eee�d���� �dd��d�d �� �Ze� d�Zdd� Z!dd� Z"e#dkr�e"�  e$ej%ej d � e$ej%ej& d � e$ej%ej& d � e$ej%ej& d � e$ej%ej& d � e$ej%ej& d � e$ej%ej& d � e$ej%ej& d  � e$ej%ej& d! � e$ej%ej& d" � e$ej%ej& d# � e$ej%ej& d$ � e$ej%ej d% � e$ej%ej& d& � e$ej%ej& d' � e$ej%ej& d( � e$ej%ej& d) � e$ej%ej& d* � e$ej%ej d+ � e$ej%ej& d, � e$ej%ej& d- � e$ej%ej& d. � e$ej%ej d/ � e$ej%ej& d0 � e$ej%ej& d1 � e$ej%ej& d2 � e'e(d3��Z)d4d5� Z*d6d7� Z+d8d9� Z,d:d;� Z-d<d=� Z.d>d?� Z/d@dA� Z0dBdC� Z1dDdE� Z2dFdG� Z3dHdI� Z4dJdK� Z5dLdM� Z6dNdO� Z7dPdQ� Z8dRdS� Z9dTdU� Z:dVdW� Z;dXdY� Z<dZd[� Z=d\d]� Z>d^d_� Z?e#dk�r�e j@�Ad`��se �Bd`� e j@�Ada��s eCdadb� e)dk�r*e*�  dS e)dck�r4e+�  dS e)ddk�r>e,�  dS e)dek�rHe-�  dS e)dfk�rRe.�  dS e)dgk�r\e/�  dS e)dhk�rfe0�  dS e)dik�rpe1�  dS e)djk�rze8�  dS e)dkk�r�e9�  dS e)dlk�r�e?�  dS e)dmk�r�e2�  dS e)dnk�r�e3�  dS e)dok�r�e4�  dS e)dpk�r�e6�  dS e)dqk�r�e7�  dS e)drk�r�e:�  dS e)dsk�r�e;�  dS e)dtk�r�e<�  dS e)duk�r�e=�  dS e)dvk�r�e>�  dS e)dwk�r�eD�  dS dS dS )x�    N��Fore�Back�StyleT�Z	autoreset��initr   c                  C   s8   dd l } g d�}|D ]}t| �t�� |� t� �� q
d S )Nr   )	� u�      ▄████████ ███    █▄     ▄████████     ███       ▄▄▄▄███▄▄▄▄      ▄████████ ████████▄  ▄██   ▄      ▄████████ u�     ███    ███ ███    ███   ███    ███ ▀█████████▄ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███   ▀███ ███   ██▄   ███    ███ u�     ███    █▀  ███    ███   ███    ███    ▀███▀▀██ ███   ███   ███   ███    █▀  ███    ███ ███▄▄▄███   ███    ███ u�    ▄███▄▄▄     ███    ███   ███    ███     ███   ▀ ███   ███   ███  ▄███▄▄▄     ███    ███ ▀▀▀▀▀▀███   ███    ███ u�   ▀▀███▀▀▀     ███    ███ ▀███████████     ███     ███   ███   ███ ▀▀███▀▀▀     ███    ███ ▄██   ███ ▀███████████ u�     ███        ███    ███   ███    ███     ███     ███   ███   ███   ███    █▄  ███    ███ ███   ███   ███    ███ u�     ███        ███    ███   ███    ███     ███     ███   ███   ███   ███    ███ ███   ▄███ ███   ███   ███    ███ u�     ███        ████████▀    ███    █▀     ▄████▀    ▀█   ███   █▀    ██████████ ████████▀   ▀█████▀    ███    █▀  ��random�printZchoice�colors�n)r   �legend�dev� r   �N   C:\Users\sence\Desktop\HasanSencer\v1.8 FuatMedya Telegram Yazılımı\main.py�
legend_dev   s
   �r   c                 C   s.   | D ]}t j�|� t j��  t�d� qd S )Ng����Mb`?)�sys�stdout�write�flush�time�sleep)�messager   r   r   r   �LEGEND_DEVty    �
   
�r   uA   =========================Telegram İletişim : t.me/fuatadmin_tr
z7=========================Developper : t.me/HasanSencer
u   Yükleniyor.....
z=--------------------------------------------------------100%
zwmic csproduct get uuidz\rr	   z\n�   zBhttps://gist.github.com/fuatmedya/0b63026dfb3516790e1e486d50028231c                 C   s.   | D ]}t |dd� tj��  t�d� qd S )Nr	   ��endg�������?)r   r   r   r   r   r   )�text�charr   r   r   �	printSlow2   r   r"   c                   C   s4   t tjv rtd� d S td� tdt  � t�  d S )N�   Giriş Başarılıu   Lisansın Etkinleştirilmemiş!uM   
Lisansının Etkinleştirilmesi İçin @fuatadmin_tr ile İletişime Geç!
 )�hwid�rr    r   �exitr   r   r   r   �Main_Program8   s
   

r'   �__main__u   Seçenekleri Belirleyiniz: u                    [1] Giriş Yapz(                 [2] Ban Filtresi Uygulaz)                 [3] Spam Filtresi Uygulau,                    [4] Hedef Gruptan Data Çeku+                    [5] Gizli Gruba Giriş Yapu+                    [6] Günlük Filtre Uygulau,                    [7] Haftalık Filtre UygulauW                    [8] Çekim Yapacağın ve Kendi Grubunda Olan Üyeleri Datadan Temizlez)                 [9] Profil Resimi Ayarlaz'                 [10] Profil Resimi Silu=                    [11] Ad-Soyad ve Kullanıcı Adı Değiştiru   Rehbere Ekleme Seçenekleri: uJ                    [12] Telegram Rehberine Ekle - Telefon Yazılımı İçinuM                    [13] Telegram Rehberine Ekle - Bilgisayar Yazılımı İçinz0                 [14] Telegram Rehberini Temizleu@                    [15] Telegram Rehberini Gruba Davet Et - Çokluz?                 [16] Telegram Rehberini Gruba Davet Et - Tekliu   Üye Ekleme Seçenekleri: z,                 [17] Gruba Davet Et - TekliuA                    [18] Gruba Davet Et - Telefon Yazılımı İçinu-                    [19] Gruba Davet Et - ÇokluzMessage Sender Option: u+                    [20] Mesaj Gönder - Tekliu,                    [21] Mesaj Gönder - Çokluu#                    [22] Çıkış Yapu   
Seçenek Belirleyiniz: c                  C   s  ddl m}  ddlm} dd l}ddlm} dd l}dd l}ddlm}m	}m
} t�  |jdd� d}	|	d7 }	td	d
��!}
|�|
�}t|�}t|	�}d}||d  |d  }W d   � n1 s`w   Y  td	d
��!}|�|�}t|�}t|	�}d}||d  |d  }W d   � n1 s�w   Y  t|�}t|�}tdd
��F}dd� |�|�D �}d}	|D ]-}|�|�}|	d7 }	t|j|j d|� � � | d|� �||�}|�|� |��  t�  q�d}W d   � n1 s�w   Y  t|r�|j|j d nd� t|j|j d � t�  d S )Nr   ��TelegramClient��utils��readerr   Tr   r   �api.csvr%   �   �numaralar.csvc                 S   �   g | ]}|d  �qS �r   r   ��.0�rowr   r   r   �
<listcomp>�   �    zlogin1.<locals>.<listcomp>�   Giriş �	sessions/u#   Tüm Numaralara Giriş Başarılı!�Hata!�1   Lütfen Çıkış Yapmak İçin Entere Basınız!)�telethon.syncr*   �telethonr,   �csvr.   �configparser�coloramar   r   r   �legend_devpostr   �open�list�int�str�parse_phoner   �BRIGHT�GREEN�start�
disconnect�RESET�YELLOW�input)r*   r,   r?   r.   r@   rA   r   r   r   �po�
api_obj_id�
csv_reader�list_of_rows�
row_number�
col_number�deltaop�hash_obj�deltaxd�api_id�api_hash�f�str_list�pphone�phone�client�doner   r   r   �login1^   sV   
�
�	

�
r`   c            !   
   C   s�  dd l } ddl m}m}m} | jdd� t�  ddlm} ddlm	} ddl
m} dd l}dd l}d}	|	d7 }	td	d
��!}
|�|
�}t|�}t|	�}d}||d  |d  }W d   � n1 s`w   Y  td	d
��!}|�|�}t|�}t|	�}d}||d  |d  }W d   � n1 s�w   Y  t|�}t|�}g }d}tdd
���}dd� |�|�D �}d}	|D ]V}|	d7 }	|�|�}td|� �� |d|� �||�}|��  |�� �sztd� t|	�}t|�}|�|� W q� |�y   td� t|	�}t|�}|�|� Y q�w t�  q�d}td� t|ddi� td� tdddd��}|j|ddd�}|�|� W d   � n	1 �s;w   Y  W d   � n	1 �sKw   Y  dd� }d d!� } |�  | �  t|�rgd"� d S d#� d S )$Nr   r   Tr   r)   r+   )�PhoneNumberBannedErrorr   r/   r%   r0   Fr1   c                 S   r2   r3   r   r4   r   r   r   r7   �   r8   zbanfilter.<locals>.<listcomp>r9   r:   u   Üzgünüm, Bu numara Banlı!ZBanu   Banlı Numaralar Listelendi!�sep�
u   BanNumers.csv'ye Kayıt Edildi�BanNumbers.csv�w�UTF-8��encoding�,�Z	delimiter�lineterminatorc               	   S   sn  dd l } dd l}g }g }g }g }g }tdd��}|D ]}|�|� qW d   � n1 s,w   Y  |D ]}	t|	��dd�}
|�|
� q3td��+}tdd��}|D ]}|�|�d	d�� qPW d   � n1 sfw   Y  W d   � n1 suw   Y  tdd��}|D ]}|�|� q�W d   � n1 s�w   Y  |D ]}t|��dd�}|�|� q�t|�}t|�}|�|�}|D ]}	|	|vr�|�|	� q�td
ddd��}| j	|dd�}|�
|� W d   � n1 s�w   Y  td
��0}tdd��}|D ]}t|��dd�}|�|� q�W d   � n	1 �sw   Y  W d   � n	1 �s!w   Y  |�d� |�d
d� td� d S )Nr   r1   r%   rc   r	   rd   zoutfile.csvre   ri   �	unban.csvrf   rg   �rk   u1   Başarılı, Tüm Banlı Numaralar Kaldırıldı.)r?   �osrC   �appendrF   �replacer   �set�intersection�writer�	writerows�remove�renamer   )r?   rn   �
collection�nc�collection1�nc1�maind�infile�line�x�mod_x�outfile�line1�i�mod_i�unique�unique1�itd�	writeFilers   �last�final�line3r   r   r   �
autoremove�   sh   ����� ��

����� 
zbanfilter.<locals>.autoremovec               	   S   s�   dd l } dd l}td��+}tdd��}|D ]}|�|�dd�� qW d   � n1 s+w   Y  W d   � n1 s:w   Y  |�d� |�dd� td� d S )Nr   r1   rl   re   ri   r	   u   Tamamlandı!)r?   rn   rC   r   rp   ru   rv   r   �r?   rn   r|   r�   r}   r   r   r   �dellst  s   ��� 
zbanfilter.<locals>.dellst�   Başarılı!r;   )rA   r   r   r   r   rB   r=   r*   r>   r,   �telethon.errors.rpcerrorlistra   r?   r@   rC   r.   rD   rE   rF   rG   r   �connect�is_user_authorizedro   rs   rt   rN   )!rA   r   r   r   r*   r,   ra   r?   r@   rO   rP   rQ   rR   rS   rT   rU   rV   rW   rX   rY   �MadeByRexhacksr_   rZ   r[   Zunparsed_phoner]   r^   �rexhacks�Nero_opr�   rs   r�   r�   r   r   r   �	banfilter�   s�   
�
�	



�	���)5r�   c            !   
      s�  dd l } ddl m� m}m� | jdd� t�  ddlm} ddlm} ddlm	}m
} ddlm} ddlm} dd l}dd l}dd	lm}	 dd l}
dd l } ddl m� m}m� | jdd� dd l}dd l}dd l}dd l}d
}d}g }d}d}tdd���}dd� |�|�D �}d}|D ]w}|�|�}|d7 }t�j� j d�j� d�j� j � d|� � � |d|� �dd�}|�|� ||jjdd�� |�|d� |� d� |�!|�}|D ]}t|j"� q�t#|�}||v r�|d7 }ntd� t#|�}|�$|� |�%�  t�  d}q�td� t|ddi� W d   � n	1 �sw   Y  t|� d�� tdd d!d"��}|j&|d#dd$�}|�'|� W d   � n	1 �sEw   Y  � �fd%d&�}d'd(� } |�  | �  t(|�rdd)� d S d*� d S )+Nr   r   Tr   r)   ��	functions�typesr+   )�YouBlockedUserErrorr-   ZSpamBotZbirdFr1   r%   c                 S   r2   r3   r   r4   r   r   r   r7   >  r8   zspambotch.<locals>.<listcomp>r   �Login � r:   ��$ � 7e14b38d250953c8c1e94fd7b2d63550z@SpamBot��idz/startu   Hesap Spamlı :( u   Spamlı Hesaplar Listelendi!rb   rc   u&    - Tane Hesap Kullanılabilir Durumda!�legend1.csvre   rf   rg   ri   rj   c               	      s�  dd l } dd l}g }g }g }g }g }tdd��}|D ]}|�|� qW d   � n1 s,w   Y  |D ]}	t|	��dd�}
|�|
� q3t�j� j d � t	� }td��.}t|� d�d	��}|D ]}|�
|�d
d�� q`W d   � n1 svw   Y  W d   � n1 s�w   Y  t|� d�d��}|D ]}|�|� q�W d   � n1 s�w   Y  |D ]}t|��dd�}|�|� q�t|�}t|�}|�|�}|D ]}	|	|vr�|�|	� q�tdd	dd��}| j|dd�}|�|� W d   � n1 s�w   Y  td��1}tdd	��}|D ]}t|��dd�}|�
|� �q	W d   � n	1 �s%w   Y  W d   � n	1 �s5w   Y  |�d� |�dd� t�j� j d � d S )Nr   r1   r%   rc   r	   u9   Spamlı Hesaplarını Nasıl Kaydetmek İstediğini Yaz :r�   z.csvre   ri   �legend2.csvrf   rg   rm   u   Görev Başarılı!)r?   rn   rC   ro   rF   rp   r   rH   rI   rN   r   rq   rr   rs   rt   ru   rv   �RED)r?   rn   rw   rx   ry   rz   r{   r|   r}   r~   r   Zrexfiler�   r�   r�   r�   r�   r�   r�   r�   rs   r�   r�   r�   �r   r   r   r   �	forremove]  sl   ����� ��

����� 
zspambotch.<locals>.forremovec               	   S   s�   dd l } dd l}td��+}tdd��}|D ]}|�|�dd�� qW d   � n1 s+w   Y  W d   � n1 s:w   Y  |�d� |�dd� |�d� d S )Nr   r1   r�   re   ri   r	   r�   )r?   rn   rC   r   rp   ru   rv   r�   r   r   r   �
deletelist�  s   ��� 
zspambotch.<locals>.deletelistr�   r;   ))rA   r   r   r   r   rB   r=   r*   r>   r�   r�   r,   r�   r�   r?   r   r.   r@   �
subprocess�requestsrn   rC   rG   r   rH   rI   �	RESET_ALLrL   rJ   �contactsZUnblockRequest�send_messager   Zget_messagesr   rF   ro   rK   rs   rt   rN   )!rA   r   r*   r�   r�   r,   r�   r?   r   r.   r@   r�   r�   rn   Zbotr�   r�   r%   r_   rZ   r[   rO   r\   r]   r^   �msgr   �
Legend_devr�   r�   rs   r�   r�   r   r�   r   �	spambotch#  sv    
0




��*r�   c            9         s@  ddl m}  dd l�dd l}dd l}dd l}ddlm} ddlm	}m
}m}m}m}	m}
m} ddlm}m} ddlm} ddlm} dd l}ddlm}m}m} |jd	d
� dd l}dd l}dd l}dd l}g d�}|�� }|�d� |d d � � }|�!d�}|d d � � }|j"|j#d� d}|d7 }t$dd��!}��|�}t%|�} t&|�}!d}"| |!d  |"d  }#W d   � n1 s�w   Y  t$dd��!}$��|$�}t%|�} t&|�}!d}"| |!d  |"d  }%W d   � n1 s�w   Y  t&|#�}&t'|%�}'�fdd���fdd�� g df�fdd�	}(� �fdd�})g }*|(g d�d d!� d}+|�(� },|,|d"d#� }-|,|d$d#� }.| d%|� �|&|'�}/|/�)�  �zG|/�*� �rVt+|j,|j- d& � z�|D ]�}0z|/||0�� W n t.�yq }1 zW Y d }1~1nd }1~1ww t+|j,|j/ |0� d'� � |D ]�}2g }3z
|/j0|0d(|2d)�}3W n t.�y� }1 zt+d*� t1�  t2�  W Y d }1~1nd }1~1ww z}|3D ]w}4t3|4j4��s��q�|4j4|*v �rq�|*�5|4j4� |4j4�r�|4j4}5nd+}5|4j6�r�|4j6}6nd,}6t7|4j8|��r�|,}7nt7|4j8|��r�|.}7t7|4j8|	��r�|-}7t7|4j8|��r|4j8j9}7|7�:d-�}8|(|+|5|4j;|6|0|8g� |+d7 }+t+|j,|j< d.|+� � d/d0� �q�W �q� t.�y> }1 zW Y d }1~1�q�d }1~1ww �qTW n t.�yU }1 zW Y d }1~1nd }1~1ww t+d1� t1�  t2�  |/�=�  t+|j,|j< d.|+� � d/d0� t+|j,|j- d2 � t+|j,|j> d3 � W n   t+|j,|j? d4 � |/�=�  Y t1�  d S )5Nr   r)   ��JoinChannelRequest��InputPeerEmpty�UserStatusOffline�UserStatusRecently�UserStatusLastMonth�UserStatusLastWeek�PeerUser�PeerChannel��datetime�	timedeltar-   )�Threadr   Tr   � �A�B�C�D�E�F�G�H�I�J�K�L�M�N�O�P�Qr�   r�   r�   r�   r�   r�   �R�S�T�U�V�W�X�Y�Z�ayarlar.ini�Redstone�	HedefGrupri   �PhoneNumber��levelr   r/   r%   r0   c                    �   t ddddd��D}� �|�}|�| d � d}tdt| ��D ]%}|�|| | d | | d | | d	 | | d
 | | d g� |d7 }qW d   � d S 1 sOw   Y  d S �N�data.csvre   �utf-8r	   �rh   �newliner   r   r0   �   �   �   �rC   rs   �writerow�range�len��usersrZ   r   �countr�   �r?   r   r   �	save_data�  �   
>
�"�zscraper1.<locals>.save_datac                    �@   t t| �d dd�D ]}| | }t|d �s| |= q
� | � d S �Nr   r   ������r�   r�   �bool�r�   r�   �user�r�   r   r   �check_users�  �   �zscraper1.<locals>.check_users�ac                    �4   t d|dd�}� j|ddd�}|�| � |��  d S �Nr�   rf   rg   ri   rc   rj   �rC   rs   r�   �close��data�moderZ   rs   r�   r   r   �update�  �   
zscraper1.<locals>.updatec                     �V   g } t dddd��}��|�}dd� |D �} W d   � n1 s w   Y  � | � d S )Nr�   r%   r�   rg   c                 S   �   g | ]}|�qS r   r   �r5   r�   r   r   r   r7   �  �    z3scraper1.<locals>.validate_data.<locals>.<listcomp>�rC   r.   �r�   rZ   �users1�r�   r?   r   r   �validate_data�  �   
�zscraper1.<locals>.validate_data�zsr. no.�usernamezuser id�name�groupZStatusre   �r  ������Zdays�����r:   r#   �(    Grubundaki Üyeler Dataya Çekiliyor...F��
aggressive�search�   Lütfen Grubu Kontrol Edin!r	   ZREDSTONE�%Y%m%d�	Toplam : �r   u   Giriş Başarısız!u   Görev tamamlandı!u)   Çıkmak için herhangi bir tuşa basın!u-   Lütfen ayarlar.ini numarasını değiştirin)@r=   r*   r?   r@   �loggingr>   �telethon.tl.functions.channelsr�   �telethon.tl.typesr�   r�   r�   r�   r�   r�   r�   r�   r�   r.   Z	threadingr�   rA   r   r   r   r   r�   r�   r   rn   �ConfigParser�read�strip�split�basicConfig�WARNINGrC   rD   rE   rF   �nowr�   r�   r   rH   rI   �	ExceptionrM   �iter_participantsrN   r&   r�   r  ro   �
first_name�
isinstance�status�
was_online�strftimer�   �MAGENTArK   rL   r�   )9r*   r@   r  r>   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r.   r�   rA   r   r   r   r�   r�   r   rn   �search_filter�configZlink1�linksr]   rO   rP   rQ   rR   rS   rT   rU   rV   rW   �API_ID�HashIDr  r  �	user_listr�   �today�	last_week�
last_monthr^   �link�er  �all_participantsr�   r  r  �date_online�date_online_strr   )r�   r?   r�   r   �scraper1�  s�   $ 


�
�	
����
"�����,��

r>  c                  C   s�  dd l } ddlm} ddlm} ddlm} dd l}| �� }|�	d� d}|d7 }t
dd��!}|�|�}t|�}	t|�}
d}|	|
d  |d  }W d   � n1 sRw   Y  t
dd��!}|�|�}t|�}	t|�}
d	}|	|
d  |d  }W d   � n1 s�w   Y  t|�}t|�}|d
 d �� }|d|� �||�}|��  |�� s�z|�|� |�|td�� td� |�|� W n |y�   td�}td� |j|d� Y nw td�}|||�� td� d S )Nr   r)   ��ImportChatInviteRequest��SessionPasswordNeededErrorr�   r   r/   r%   r0   r�   r�   r:   �
Kodu Gir: r	   �   2fa Şifresini Gir: ��passwordzGizli Grubun Hash Kodunu Gir : u   Gruba Giriş Başarılı!)r@   r=   r*   �telethon.tl.functions.messagesr@  �telethon.errorsrB  r?   r!  r"  rC   r.   rD   rE   rF   r#  r�   r�   �send_code_request�sign_inrN   r   )r@   r*   r@  rB  r?   r1  rO   rP   rQ   rR   rS   rT   rU   rV   rW   r3  r4  r]   r^   rF  Zgplinkr   r   r   �privategroupJoiner$  sT   

�
�	
�rK  c            $         sh  t �  ddlm} m} dd l}dd l}ddlm} m} ddlm�	m� ddlm	� dd l
�dd l}ddlm} ddlm}m�m�m�m�m}m} dd l}	dd l}
dd l}ddlm� m}m� |jd	d
� g d��|	�� }|�d� |d d �� }|�d�}d}|d7 }tdd��!}�� |�}t!|�}t"|�}d}||d  |d  }W d   � n1 s�w   Y  tdd��!}�� |�}t!|�}t"|�}d}||d  |d  }W d   � n1 s�w   Y  t"|�}t#|�}|d d �� }|j$|j%d� �fdd��
�
fdd��g df�fdd�	���fdd�}� �������	���fdd �}t&�j'� j( d! � t"t)� �}|}�	�*� �| d"� �+d#�}g } t&�j'� j, d$|� � � z2| d%|� �||�}!|!�-�  |!�.� �rut&�j'� j/ d& � ||!||�}"nt&�j'� j0 |� d'� � W n t1�y� }# z
t&|#� W Y d }#~#nd }#~#ww t&�j'� j/ d( � t&�j'� j( d) � t)�  d S )*Nr   �r*   �
connection�r*   �syncr�   r�   �r�   r�   r   Tr   r�   r�   r�   r�   ri   r   r/   r%   r0   r�   r�   c                    r�   r�   r�   r�   r�   r   r   r�   �  r�   zdailyfilter.<locals>.save_datac                    r�   r�   r�   r�   r�   r   r   r�   �  r�   z dailyfilter.<locals>.check_usersr�   c                    r�   r�   r�   r�   r�   r   r   r  �  r  zdailyfilter.<locals>.updatec                     r  )Nr�   r%   r�   rg   c                 S   r  r   r   r  r   r   r   r7   �  r  z6dailyfilter.<locals>.validate_data.<locals>.<listcomp>r  r	  r  r   r   r  �  r  z"dailyfilter.<locals>.validate_datac                    �*  �� � }|�	dd� }|�	dd� }|�d�}�
g d�dd� d}g }|D ]�}| �|�}	z| �|�� W n tyF }
 zW Y d }
~
nd }
~
ww t�j� j |� d	� � �D ]�}g }z
| j|d
|d�}W n ty� }
 ztd� t�  t	�  W Y d }
~
nd }
~
ww z|D ]z}t
|j�s�q�|j|v r�q�|�|j� zat|j��r�|}nt|j��r�|}t|j��r�|}t|j��r�|jj}|�d�}t|�t|�kr�|t|j�t|j�t|jd |j �|t|�g}�
|� t�j� j d|� � dd� |d7 }W q�   Y q�W qV   Y qVq%td|� | ��  t�  d S �Nr  r  r  r  r  re   r  r   r  Fr  r  r�   r  r  r   �r'  r.  �
get_entityr(  r   rH   rM   r)  rN   r&   r�   r  ro   r+  r,  r-  rF   r�   r*  �	last_namer/  rK   �r^   r9  �last_dayr6  r7  r8  r�   r5  r�   r  r:  r  r;  r�   r<  r=  �b�r   r�   r   r�   r�   r�   r�   r�   r0  r�   r  r   r   �nfilter�  �z   

����


����
%
zdailyfilter.<locals>.nfilter�   
Filtre için günü girin:r  r  �   
Giriş Yapılıyor r:   r#   �    Giriş Başarısız�   Filtreleme Başarılı�4   Lütfen Çıkmak İçin Herhangibir Tuşa Basınız!�2rB   r>   r*   rM  r  rO  r�   r�   r  r�   r?   �jsonr   r�   r�   r�   r�   r�   r�   r�   r@   �uuidrA   r   r   r   r   r!  r"  r#  r$  rC   r.   rD   rE   rF   r%  r&  r   rH   rM   rN   r'  r.  rL   r�   r�   rI   r�   r(  �$r*   rM  r  r>   rO  rb  r�   r�   r�   r@   rc  rA   r   r1  r2  r9  rO   rP   rQ   rR   rS   rT   rU   rV   rW   r3  r4  r]   r  rZ  r   rW  Zdeler^   r�   r:  r   �r   r�   r   r�   r�   r�   r�   r�   r?   r�   r�   r0  r�   r  r   �dailyfilterT  s�   $


�
�		 8

���
rf  c            $         s|  t �  ddlm} m} dd l}dd l}ddlm} m} ddlm�	m� ddlm	� dd l
�dd l}ddlm} ddlm}m�m�m�m�m}m} dd l}	dd l}
dd l}ddlm� m}m� ddlm� m}m� |jd	d
� g d��|	�� }|�d� |d d �� }|�d�}d}|d7 }tdd��!}�� |�}t!|�}t"|�}d}||d  |d  }W d   � n1 s�w   Y  tdd��!}�� |�}t!|�}t"|�}d}||d  |d  }W d   � n1 s�w   Y  t"|�}t#|�}|d d �� }|j$|j%d� �fdd��
�
fdd��g df�fdd�	���fdd�}� �������	���fdd �}t&�j'� j( d! � t"t)� �}|}�	�*� �| d"� �+d#�}g } t&�j'� j, d$|� � � z2| d%|� �||�}!|!�-�  |!�.� �rt&�j'� j/ d& � ||!||�}"nt&�j'� j0 |� d'� � W n t1�y� }# z
t&|#� W Y d }#~#nd }#~#ww t&�j'� j/ d( � t&�j'� j( d) � t)�  d S )*Nr   rL  rN  r�   r�   rP  r�   r   Tr   r�   r�   r�   r�   ri   r   r/   r%   r0   r�   r�   c                    r�   r�   r�   r�   r�   r   r   r�   !  r�   zweeklyfilter.<locals>.save_datac                    r�   r�   r�   r�   r�   r   r   r�   *  r�   z!weeklyfilter.<locals>.check_usersr�   c                    r�   r�   r�   r�   r�   r   r   r  1  r  zweeklyfilter.<locals>.updatec                     r  )Nr�   r%   r�   rg   c                 S   r  r   r   r  r   r   r   r7   ;  r  z7weeklyfilter.<locals>.validate_data.<locals>.<listcomp>r  r	  r  r   r   r  7  r  z#weeklyfilter.<locals>.validate_datac                    rQ  rR  rS  rV  rY  r   r   rZ  >  r[  zweeklyfilter.<locals>.nfilterr\  r  r  r]  r:   r#   r^  r_  r`  ra  rd  r   re  r   �weeklyfilter�  s�   $


�
�		 8

���
rg  c            G         s�  ddl m} m} dd l}dd l }ddl m}m} m} ddlm} ddlm	}m
}m}	m}
m}m}m} dd l}ddlm}m}m}m} ddlm}m} dd l� dd l}dd l}dd l}dd l}ddlm}m}m} |j d	d
� t!�  dd l"}dd l}dd l#}|j$|j%d� |�&� }|�'d� |d d �(� }d} | d7 } t)dd��!}!� �*|!�}"t+|"�}#t,| �}$d}%|#|$d  |%d  }&W d   � n1 s�w   Y  t)dd��!}'� �*|'�}"t+|"�}#t,| �}$d}%|#|$d  |%d  }(W d   � n1 s�w   Y  t,|&�})t-|(�}*|d d �(� }+t)dddd��},� �*|,�}-dd� |-D �}.W d   � n	1 �s&w   Y  t)dddd��},� �*|,�}-dd� |-D �}/W d   � n	1 �sJw   Y  | d|+� �|)|*�}0|0�.�  |0�/� �sjt0d|+� d�� n�g }1d }2d}3g }4d}5|5dk�rEz�|0�1|�}6|6j2d	k�r�t-|6j3�}7|0j4|6dd �}8g }9g }:d};g }<|8D ]"}=zt-|=j3�|/v �r�|<�5|/�6t-|=j3��� W �q�   t0d!� Y �q�|,�7�  |0�8�  |<j9d	d"� |<D ]}>|.|>= �q�t)dd#dd$d%��},� �:|,�}?|?�;|.� W d   � n	1 �s�w   Y  d}5n
t0|j<|j= d& � d}5W n7 |j>j?j@�y   |0||�� Y n% tA�y0   t0|j<|jB d' � d}5Y n   t0|j<|j= d( � d}5Y |5dk�syt+� }@� fd)d*�}A� fd+d,�}B|A�  |B�  t)d-dd.d��U}C� �*|C�}Dt)dd#d.d��8},� j:|,d/d0d1�}E|E�Cg d2�� d}>|DD ]}F|>d7 }>|E�C|>|Fd |Fd |Fd3 |Fd4 |Fd5 f� �q�W d   � n	1 �s�w   Y  W d   � n	1 �s�w   Y  |�Dd6� |�Dd-� t0|j<|jE d7 � t0|j<|jB d8 � t0|j<|jF d9 � tG�  d S ):Nr   rL  )rO  r*   �events��GetDialogsRequestr�   ��GetChannelsRequest�GetFullChannelRequestr�   �InviteToChannelRequestr�   r   Tr   r�   r�   r�   �	BizimGrupr   r/   r%   r0   r�   r�   r�   rg   c                 S   r  r   r   r  r   r   r   r7   �  r  z!Deletealready.<locals>.<listcomp>c                 S   s   g | ]}t |d  ��qS )r0   )rF   r  r   r   r   r7   �  s    r:   u)   
Giriş Başarısız, Lütfen Öncelikle u    Giriş Yap
��   r�   F)r  u   Kullanıcı Çekme Hatası!)�reversere   r	   r�   u   
Hatalı Grup...
u   
Yalnızca Genel Gruplar...
u   
Geçersiz Grup...
c                     �   t � } tdddd��%}� �|�}|D ]}| �|� |D ]}|dkr&| �|� qqW d   � n1 s2w   Y  tdddd��}� j|dd	d
�}|�| � W d   � d S 1 sWw   Y  d S )Nr�   r%   rf   rg   r	   �1.csvre   ri   rc   rj   �rD   rC   r.   ro   ru   rs   rt   ��linesZreadFiler.   r6   Zfieldr�   rs   r�   r   r   �main�  s    


����"�zDeletealready.<locals>.mainc                     rr  )Nrs  r%   rf   rg   r  �2.csvre   ri   rc   rj   rt  ru  r�   r   r   �main1  s    


����"�zDeletealready.<locals>.main1rx  rf   ri   rc   rj   r  r�   r�   r�   rs  u'   Çakışan Üyeler Başarıyla Silindi!u   Görev Başarılır<   )Hr>   r*   rM  r  rO  rh  rG  rj  r   r�   r�   r�   r�   r�   r�   r�   rb  r  rl  rm  r�   rn  r�   r�   r?   r   r   r@   rA   r   r   r   r   rB   r�   rn   r%  r&  r!  r"  r#  rC   r.   rD   rE   rF   r�   r�   r   rT  Z	megagroupr�   r)  ro   �indexr�   rK   �sortrs   rt   rH   r�   �errorsZrpcerrorlist�ChatWriteForbiddenError�
ValueErrorrI   r�   ru   rL   rM   rN   )Gr*   rM  r  r>   rO  rh  rj  r�   r�   r�   r�   r�   r�   r�   rb  rl  rm  r�   rn  r�   r�   r   r   r@   rA   r   r   r   r�   rn   r1  r9  rO   rP   rQ   rR   rS   rT   rU   rV   rW   r3  r4  r]   rZ   r
  r�   Zuserlistr^   ZchatsZ	last_dateZ
chunk_sizeZgroupsr   r  Zgroup_idr;  ZresultsZresults1r�   Zindex1r�   r�   r   rv  rw  ry  �sourceZrdrrs   r6   r   r�   r   �Deletealready�  s�   $

�
�	
�
�



�

�
�%
.����


r�  c            !         s�  ddl m� dd l�ddlm}  ddlm}m}m}m	} ddl
m}m}m}m} ddlm}	 ddlm}
m�m�m�	 dd l}ddl
m}m}m} dd l}dd l�dd l�dd	lm� dd
lm} ddl m!}m"� |�  �j#��j$}�j%�
�j&��j'��fdd�}|�  t(�  d}|d7 }t)dd��!}��|�}t*|�}t+|�}d}||d  |d  }W d   � n1 s�w   Y  t)dd��!}��|�}t*|�}t+|�}d}||d  |d  }W d   � n1 s�w   Y  t+|�� t,|��g }t)dd��}�|�}t-|�}|D ]} |�.t+| d �� �qW d   � n	1 �sw   Y  |�t/|� d�
� d�� t,t0|��� �
� �� � ��������	�
�������fdd����
�fdd����  d S )Nr   r)   ri  �r�   �InputPeerChannel�InputPeerUserr�   ��PeerFloodError�UserPrivacyRestrictedErrorr}  �UserAlreadyParticipantError�rn  �r�   r,   r|  r�   ��UsernameInvalidError�ChannelInvalidErrorra   r-   ��StringSessionr   c                      �&   � j dkr� �d� d S � �d� d S �N�nt�cls�clear�r  �systemr   �rn   r   r   �clrY  �   
zaddcontactforphone.<locals>.clrr   r/   r%   r0   r1   �Toplam Hesap: r�   c                      s2  t t�� d�	� ���d } t t�� d�	� ���}t t�� d�	� ���}t t�� d�	� ���}tdddd	��}�j|d
dd�}|�||| g� W d   � n1 sQw   Y  d}d}�| |� D �]�}|d7 }td|� �� ��|�}	ttj�j	 dtj
� dtj�j � d|	� � � �d|	� �� ��}
|
��  |
�� s�t�� d�	� �� |
�|	� |
�|	td�� d}g }t|dd	��;}�j|d
dd�}t|d � |D ]#}i }|d |d< |d |d< t |d �|d< |d |d< |�|� q�W d   � n1 s�w   Y  tdd��}�|�}t|�}d}d}||d  |d  }W d   � n	1 �s&w   Y  t |�}|| }tdd��}�|�}t|�}d}d}||d  |d  }W d   � n	1 �sZw   Y  t |�}|| }tdddd	��}�j|d
dd�}|�||g� W d   � n	1 �s�w   Y  d}|D ]w}t |�t |d �k�rt |d �t |�k�rz/|d7 }|d dk�r�t�� d�	� �� W �q�|
�jj|d |d dddd �� |� d!�}W n* �j�y� } z
|jj}W Y d }~nd }~w   ���  t�� d"�	� �� Y �q�t|� �q�|d7 }q`�
�d� ��  d S )#N�Bu Hesaptan : r   �Bu Hesapa Kadar : u)   Eklemeye Nerden Başlamak İstiyorsun? : u    Bir Hesap Kaç Kişi Eklesin? : �
memory.csvre   rf   rg   ri   rc   rj   r   �Index : r9   r�   r:   u   Bir Şeyler Ters Gitti :(zKodu Gir : r�   �srnor  r0   r�   r�   r  r%   r	   �'   username yok, bir diğerine geçiyorum.ZgdfT)r�   r*  rU  r]   Zadd_phone_privacy_exceptionu    - başarılı �Unexpected Error)rE   rN   rC   rs   r�   r   rG   r   rH   rI   r�   rL   r�   r�   rI  rJ  r.   �nextro   rD   r�   ZAddContactRequest�RPCError�	__class__�__name__�	print_excru   ) �From�Upto�rex�hacks�filers   r�   �indexx�xdr]   r^   �
input_filer�   rZ   �rowsr6   r�   rV   rQ   rR   rS   rT   �numnext�	startfrom�	nextstart�numend�endto�nextend�df�itr,  r:  )r3  r   r4  r*   �again�blr?   r|  r�   r   rn   r\   r%   r.   �	tracebackr,   �yer   r   �autos�  s�   �
0

���	��,���


z!addcontactforphone.<locals>.autosc                     s.   t �� d�� ��} | dkr� �  d S t�  d S )Nua   Başarılı!
Seçenek Belirleyiniz:

1 - Scripti Tekrar Et.
Entere Bas ve Çıkış Yap.

Enter: �1)rN   �quit)�stat)r�  r   r%   r   r   r�  �  s   

z!addcontactforphone.<locals>.again)1r=   r*   r?   rG  rj  r   r�   r�  r�  r�   r�   r�  r�  r}  r�  r  rn  r>   r�   r,   r|  r�   r@   r�  r�  ra   �rern   r�  r.   �telethon.sessionsr�  rA   r   r   �LIGHTRED_EXrI   rL   �BLUErM   rB   rC   rD   rE   rF   �tuplero   r   r�   )!rj  r�   r�  r�  r�   r�  r�  r}  r�  rn  r�   r@   r�  r�  ra   r�  r�  r   �grr�  rO   rP   rQ   rR   rS   rT   rU   rV   rW   r]   �	delta_obj�list_of_phone�phone_r   )r3  r   r4  r*   r�  r�  r�  r?   r|  r�   r   rn   r\   r%   r.   r�  r,   r�  r   �addcontactforphone<  sn   
�
�	��(,i
r�  c                  C   s`   dd l } ddl m}m}m} | jdd� t�  t|j|j d � t|j|j d � t	�  d S )Nr   r   Tr   u1   Addcon Klasöründen automarge.py'yi Çalıştırr<   )
rA   r   r   r   r   rB   r   rH   rM   rN   )rA   r   r   r   r   r   r   �forpc�  s   
r�  c            "      C   s:  ddl m}  dd l}t�  ddlm}m}m} ddlm	} ddl
m}m}m} dd l}	ddlm}
m}m}m} ddlm} ddlm}m} dd	lm} dd l}dd
lm}m}m} |jdd� tdd��}dd� |� |�D �a!W d   � n1 syw   Y  t"dt#t$t!�� � t%t&d��d }t%t&d��}d}da't!||� D ]z}|d7 }t"d|� �� |�(|�}t"d|� �� | d|� �dd�}|�)|� ||dd��}d}|j*D ]F}|d7 }z|||gd�� t"|j+|j, |� d|j-� d� � W q� |j.�y }  z| j/j0}!t"|� d|j-� d|!� �� W Y d } ~ q�d } ~ ww q�d S )Nr   r)   r�  r?  �r�   r,   r|  rk  �r�   )�GetContactsRequest�DeleteContactsRequest��AddChatUserRequestr   Tr   r1   r%   c                 S   r2   r3   r   r4   r   r   r   r7     r8   z!Deletecontact.<locals>.<listcomp>r�  r�  r   r�  r�  r9   r:   iDD  Z5bdea166e6097ce98a23��hashr�   � - z - Silindi.)1r=   r*   r?   rB   r�   r�  r�  ra   rG  r@  r>   r�   r,   r|  r�  r  rl  rm  r�   rn  r   r�   �telethon.tl.functions.contactsr�  r�  r�  rA   r   r   r   r   rC   r.   �phlistr   rF   r�   rE   rN   ZrexhacksprorG   rJ   r�   rH   rI   r�   r�  r�  r�  )"r*   r?   r�  r�  ra   r@  r�   r,   r|  r�  rl  rm  r�   rn  r�   r�  r�  r�  rA   r   r   r   rZ   �Rexhacks_ne_script_banaya_hai�2telegram_script_banyane_ke_liye_rexhacks_ko_dm_kror�  Zrexhacksonytr]   r^   r�   ZrexaddZrexopr:  �error   r   r   �Deletecontact  sX   �


&����r�  c                  C   sT   dd l } g d�}|D ]}t| �t�� |� t� �� q
tdt� �� tdt� �� d S )Nr   )r	   u�   ███████╗██╗   ██╗ █████╗ ████████╗███╗   ███╗███████╗██████╗ ██╗   ██╗ █████╗u�   ██╔════╝██║   ██║██╔══██╗╚══██╔══╝████╗ ████║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗u�   █████╗  ██║   ██║███████║   ██║   ██╔████╔██║█████╗  ██║  ██║ ╚████╔╝ ███████║u�   ██╔══╝  ██║   ██║██╔══██║   ██║   ██║╚██╔╝██║██╔══╝  ██║  ██║  ╚██╔╝  ██╔══██║u�   ██║     ╚██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║███████╗██████╔╝   ██║   ██║  ██║u�   ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚══════╝╚═════╝    ╚═╝   ╚═╝  ╚═╝u@   =========================Telegram İletişim : t.me/fuatadmin_tru?   =========================Telegram İletişim : t.me/HasanSencerr
   )r   ZLegendr   r   r   r   rB   4  s   rB   c            8      C   s�  dd l } ddl m}m}m} | jdd� t�  ddlm} dd l}ddl	m
}m}m} ddlm}	 ddlm}
m}m} dd l}dd l}dd	lm} dd
lm}m}m}m} ddlm} ddlm} ddlm} ddl m}m}m} dd l }|�!� }|�"d� |d d }|d d }|d d }|d d }|d d }t#dd��}dd� |�$|�D �}W d   � n1 s�w   Y  t%dt&t'|�� � t%|j(|j) d � t*� } t%|j(|j) d � t+t*� �}!t%|j(|j) d � t+t*� �}"| dkr�t+|�}#|}$n| dk�rt+|�}#|}$t+|�}%t+|�d }&t+|�}'d}(da,||&|'� D �]})|(d7 }(|�-|)�}*t%d |*� �� |d!|*� �d"d#�}+|+�.|*� t%d$|(� �� z	|+�/||#��},W n4 t0�y�   | dk�rj|+|	|$�� |+�1||#��},n| dk�r�|+||$�� |�2d%� |+�1||#��},Y nw |+||,d&��}-t+|-j3j4�a,t%d't,� �� t,|%k�r�t%d(|%� d)�� t*�  t5�  |+|dd*��}.|.j6}/t'|/�}0t%d+|0� �� d}1d}2|1|0k �r=d,d� |/d |!� D �}3zD|�2|"� |+|j7j|#|3d-�� |1|!7 }1t8dd.�D ]}4z|/|4= W �q� t9�y	 }5 zW Y d }5~5�q�d }5~5ww t%|j(|j) d/|1� � � W n |j:�y7 }6 z|6j;j<}7t%t&|7�� W Y d }6~6�qd }6~6ww |1|0k �sɐqd S )0Nr   r   Tr   r)   r�  r?  r�  �r�   rk  r�  �r�  r�  r�   r�   ro  �GroupID�	EnterStop�StartingAccount�
EndAccountr1   r%   c                 S   r2   r3   r   r4   r   r   r   r7   e  r8   zbulkadder.<locals>.<listcomp>�Total account: �7   Gizli Grup ise Y Genel Grup ise N'ye basınız.(Y/N) : u"   Kaç Üye Eklemek İstiyorsunuz : u*   Gecikme Süresi Ayarlayın (0 Hiç Demek) r�   r�   r   r�   r:   i��" Z 85468d44607fcb5b9efe5ed61e4582a2r�  r�   ��channel�	   Üyeler: �Hedef �    Tamamlandı!r�  r  c                 S   r  r   r   )r5   Zdeltar   r   r   r7   �  r  �r�  r�   �
   zParti: )=rA   r   r   r   r   rB   r=   r*   r?   r�   r�  r�  ra   rG  r@  r>   r�   r,   r|  r�  r   r�   r  rl  rm  r�   rn  r   r�   r�  r�  r�  r@   r!  r"  rC   r.   r   rF   r�   rH   rI   rN   rE   ZLegenddev_is_main_developerrG   rJ   rT  r~  �get_input_entityr   �	full_chat�participants_countr�  r�   �channelsr�   r(  r�  r�  r�  )8rA   r   r   r   r*   r?   r�  r�  ra   r@  r�   r,   r|  r�  r   r�   rl  rm  r�   rn  r�   r�  r�  r@   r1  �	grouplink�groupid�stopnum�stacno�endacnorZ   r�  �prchkZLegenddevismainr�   r�   �prlink�stopZ
start_fromZuptor�  Zpythondeveloperr]   r^   r�  �channelinfoZmembersZuser_to_addZcountconZ
batchcountZlolZsemenr�   r�   r:  r�  r   r   r   �	bulkadderB  s�   
�







��	


�����
���r�  c            1      C   s�  dd l } ddl m}m}m} | jdd� t�  ddlm} dd l}ddl	m
}m}m} ddlm}	 ddlm}
m}m} dd l}dd	lm}m}m}m} dd
lm} ddlm} ddlm} ddl m}m}m} dd l}dd l}|� � }|�!d� |d d }|d d }|d d }|d d }|d d }t"dd��}dd� |�#|�D �}W d   � n1 s�w   Y  t$dt%t&|�� � t$|j'|j( d � t)� }t$|j'|j( d � t*t)� �} |dkr�t*|�}!|}"n
|dkr�t*|�}!|}"t*|�}#t*|�d }$t*|�}%d}&da+||$|%� D ]�}'|&d7 }&t$d|&� �� |�,|'�}(t$d|(� �� |d |(� �d!d"�})|)�-|(� z	|)�.||!��}*W n4 t/�yl   |dk�rS|)|	|"�� |)�0||!��}*n|dk�rj|)||"�� |�1d#� |)�0||!��}*Y nw |)||*d$��}+t*|+j2j3�a+t$d%t+� �� t+|#k�r�t$d&|#� d'�� t)�  t4�  |)|dd(��},d}-|,j5D ]T}.|-d7 }-z"|)||!|.gd)�� t$|j'|j( |-� d*|.j6� d+� � |�1| � W �q� |j7�y� }/ z|/j8j9}0t$|j'|j: |-� d*|.j6� d*|0� � � W Y d }/~/�q�d }/~/ww �qd S ),Nr   r   Tr   r)   r�  r?  r�  rk  r�  r�  r�  r�   r�   ro  r�  r�  r�  r�  r1   r%   c                 S   r2   r3   r   r4   r   r   r   r7   �  r8   zsingle.<locals>.<listcomp>r�  r�  �,   Gecikme Süresi Ayarlayın (0 Hiç Demek) : r�   r�   r   r�  r�   r:   �� + � 5f34bd560b5053ae7edc32b5c0246245r�   r�  r�  r�  r�  r�  r�  r�  u    - Başarılı);rA   r   r   r   r   rB   r=   r*   r?   r�   r�  r�  ra   rG  r@  r>   r�   r,   r|  r�  r  rl  rm  r�   rn  r   r�   r�  r�  r�  r   r@   r!  r"  rC   r.   r   rF   r�   rH   rI   rN   rE   ZRExhacksprorG   rJ   rT  r~  r�  r   r�  r�  r�  r�   r�   r�  r�  r�  r�   )1rA   r   r   r   r*   r?   r�  r�  ra   r@  r�   r,   r|  r�  rl  rm  r�   rn  r�   r�  r�  r   r@   r1  r�  r�  r�  r�  r�  rZ   r�  r�  r�   r�   r�  r�  r�  r�  r�  rW   r]   r^   r�  r�  r�   ZdeltaaddrU   r:  r�  r   r   r   �single�  s�   
�





��	

"&����r�  c                  C   s�  dd l } ddl m}m}m} | jdd� t�  ddlm} ddlm	}m
} ddlm} ddlm} dd l}ddlm}	 dd l}
ddl m}m}m} dd l}dd l}dd l}dd l}d	}td
d��O}dd� |�|�D �}d}|D ]8}|�|�}|d7 }t|j|j |� d� � |d|� �dd�}|�|� ||jj|�d�d��}td� d}qoW d   � n1 s�w   Y  t|r�d� d S d� d S )Nr   r   Tr   r)   r�   r+   r-   Fr1   r%   c                 S   r2   r3   r   r4   r   r   r   r7     r8   zsetprofile.<locals>.<listcomp>r   u    Değiştiriliyor.r:   r�  r�  zset.jpg)r�  u6   Profil Resimi Başarılı Bir Şekilde Değiştirildi!r�   r;   )rA   r   r   r   r   rB   r=   r*   r>   r�   r�   r,   r?   r.   r@   r�   r�   r   rn   rC   rG   r   rH   rI   rJ   ZphotosZUploadProfilePhotoRequestZupload_filerN   )rA   r   r   r   r*   r�   r�   r,   r?   r.   r@   r�   r�   r   rn   r_   rZ   r[   rO   r\   r]   r^   �resultr   r   r   �
setprofile
  s>    

���r�  c                  C   s�  dd l } ddl m}m}m} | jdd� t�  ddlm} ddlm	}m
} ddlm} ddlm} ddlm} dd l}	dd	lm}
 dd l}ddl m}m}m} dd l}dd l}dd l}dd l}d
}tdd��R}dd� |	�|�D �}d}|D ];}|�|�}|d7 }t|j|j |� d� � |d|� �dd�}|�|� |||�d��� t|j|j d � d}quW d   � n1 s�w   Y  t|r�d� d S d� d S )Nr   r   Tr   r)   r�   )�DeletePhotosRequestr+   r-   Fr1   r%   c                 S   r2   r3   r   r4   r   r   r   r7   >  r8   z!Deleteprofile.<locals>.<listcomp>r   z Siliniyor...r:   r�  r�  �meu)   Profil Resimi Başarıyla Değiştirildi.r�   r;   )rA   r   r   r   r   rB   r=   r*   r>   r�   r�   Ztelethon.tl.functions.photosr�  r,   r?   r.   r@   r�   r�   r   rn   rC   rG   r   rH   r�   rJ   Zget_profile_photosrI   rN   )rA   r   r   r   r*   r�   r�   r�  r,   r?   r.   r@   r�   r�   r   rn   r_   rZ   r[   rO   r\   r]   r^   r   r   r   �Deleteprofile+  s<    

��r�  c                     s  dd l } ddl m�m}m�
 | jdd� t�  ddlm� ddlm	} ddl
m}m}m}m} ddlm�m�m�m� dd	lm� dd
lm�m� ddlm�	 ddlm}m�m� dd l}dd l}	ddlm �m!}
m�m�m"�m#�m$}m%}m&�m� dd l'�ddl'm(} dd l)�dd l*�dd l+�dd l } ddl m�m}m�
 | jdd� ddl,m-} t.�
j/�j0 d � t1t2� �}t3dd��}||�}t4|�}|}d}||d  |d  }W d   � n1 s�w   Y  d}|d7 }t3dd��!}��(|�}t4|�}t1|�}d}||d  |d  }W d   � n	1 �sw   Y  t3dd��!}��(|�}t4|�}t1|�}d}||d  |d  }W d   � n	1 �sBw   Y  t1|�� t5|��|�|�6� }|�7d� |d d �� ���������	�
��������������fdd�}|�  d S )Nr   r   Tr   r)   ri  r�  r�  r�  �rm  r�   rA  r�  )
�FloodWaitError�UserDeactivatedBanErrorr�  r�  �UserNotMutualContactError�UserChannelsTooMuchErrorr�  �UsernameNotOccupiedError�UserBannedInChannelErrorr}  r-   r�  �-   Hangi Hesabı Kullanmak İstiyorsun?

Enter: r1   r%   r   r/   r0   r�   r�   ro  c                     s�  �} �� ��}�d|� �� ��}|��  |�� sHz|�|� |�|td�� td� |�|� W n �	yG   td�}td� |j|d� Y nw |�� }|jsS|j	}n|j	d |j }|j
}d}g }t|dd	��;}	�j|	d
dd�}
t|
d � |
D ]#}i }|d |d< |d |d< t|d �|d< |d |d< |�|� qxW d   � n1 s�w   Y  ttd��}ttd��}|D �]�}t|�t|d �k�rNt|d �t|�k�rNz6d}|d dkr�td� W q�|�| |d g�� �
j�j d }t�
j�j d � ����dd�� W �n	 ��y#   �
j�j d }����dd�� Y n� ��y6   t�
j�j d � Y n� ��y] } zd }t�
j�j d! � ����d"d#�� W Y d }~n�d }~w ��y } z|j}td|� d$�� ��|� W Y d }~n�d }~w ��y� } z|�| �� ��d� W Y d }~q�d }~w ��y�   �
j�j d% }Y ne ��y�   �
j�j d& }Y nT ��y�   t�
j�j d'|� d(� � ��d)� Y n8 �j�y� } z
|jj}W Y d }~n%d }~w t�y } z|}W Y d }~nd }~w   ���  td*� Y q�|�| �}|�|d+��}t|jj�}t�
j�j d|� d�
j�j � d,|� �
j � d�
j�j! � d-|d � d.|� � � q�t|d �t|�k�rctd/� t�  t"�  q�d S )0Nr:   rC  r	   rD  rE  r�   r�   rf   rg   ri   rc   rj   r   r�  r   r  r0   r�   r�   r  zBu Hesaptan = zBu Hesapa Kadar = r�   u%   username yok, diğerine geçiyorum...r�   u   Lütfen Bekle...�   �   u3   Gizlilik Ayarları Bu Kullanıcıya İzin Vermiyor.r�   u   Bu üye zaten grupta!�Hesap Spamda!u   Hesabı Lütfen Dinlendir...i�� i@B z saniye bekle...u"   Kullanıcı Çok Fazla Gruba Üye!u3   Karşıdaki Kullanıcı İle İletişim Kurulmuyor!z
Bu Numara u    Sınırsız Spam Yemiş!i`�  zBeklenmeyen Hatar�  u    > Grup Üyesi �>> � >> u   Ekleme Başarıyla Tamamlandı!)#rG   r�   r�   rI  rJ  rN   r   �get_merU  r*  r]   rC   r.   r�  rE   ro   rH   rI   rM   r   �	randranger�   �secondsr�  r�  r�  r(  r�  rT  r�  r�  rL   r�   �CYANr&   )�channel_usernamer]   r^   rF  r�   �
LegendNameZLegendPhoner�  r�   rZ   r�  r6   r�  r�  r,  �g�t�stime�cwfer:  �dZchannel_connectZchannel_full_infoZcountt�r3  r}  r   r   rm  r4  rn  r�   r�  rB  r   r*   r�  r  r  r  r�  r?   r|  r\   r   r   �to_groupr�  r,   r   r   r�  �  s�   

�
��
,��
���
T��zAdder.<locals>.autos)8rA   r   r   r   r   rB   r=   r*   rG  rj  r   r�   r�  r�  r�   r�   r�  r�  r}  r�  r  rn  rm  r�   rH  rB  r>   r�   r,   r|  r@   r   r   r  r  r  r�  r  r  r?   r.   r�  r   r   r�  r�  r   rH   rM   rE   rN   rC   rD   rF   r!  r"  )rA   r   rj  r�   r�  r�  r�   r�   r@   r   r  r�  r  r.   r�  �Legend_devinput�read_objrQ   rR   rS   rT   �valuerO   rP   rU   rV   rW   r1  r�  r   r  r   �AdderJ  sr   0
�
�
�	
<
ir  c            !         s�  ddl m� ddlm} m�m�m} dd l�ddlm	� ddl
m}m� ddlm}m}m}m} ddlm}m}m� m}	 ddlm} dd	lm}
m�m�
m� dd l}dd
lm}m}m} dd l}dd l �dd l!�ddlm"� ddl#m$} ddl%m&}m'� dd l(�dd l)}|�  �j*��j+}�j,��j-}�j.��fdd�}|�  dd l%}ddl%m'�m/}m0� |j&dd� t1�  |�2� }|�3d� |d d �|d d �|d d �|d d �|d d �	g }t4dd��}�|�}t5|�}|D ]}|�6t7|d �� q�W d   � n	1 �sw   Y  |�t8|� d�� d�� t9t:|��� �� �� � ��������	�
��������������fdd�}� ��������	�
��������������fd d!�}t9t;|� d"�� ���} | d#k�rp|�  d S | d$k�rz|�  d S d S )%Nr   r)   rk  r�  )rj  r@  r�  r�  r�  r�  r�  r-   r�  r   c                      r�  r�  r�  r   r�  r   r   r�    r�  zadderforphone.<locals>.clrr   Tr   r�   r�   ro  r�  r�  r�  r�  r1   r%   r�  r�   c            )         s�  t �j�j d � tt� �} d}t��}t��}t��d }t��}td�}td�d }t��}tdddd��}	�j|	d	d
d�}
|
�||| g� W d   � n1 sTw   Y  d}d}�||� D �]�}|d7 }t d|� �� ��	|�}t d|� �� �d|� �dd�}|�
�  |�� s�t �� d�� �� |�|� |�|td�� |}g }t|dd��;}�j|d	d
d�}t|d � |D ]#}i }|d |d< |d |d< t|d �|d< |d |d< |�|� q�W d   � n1 s�w   Y  tdd��}�|�}t|�}d}d}||d  |d  }W d   � n	1 �sw   Y  t|�}|| }tdd��}�|�}t|�}d}d}||d  |d  }W d   � n	1 �sLw   Y  t|�}|| } tdddd��}!�j|!d	d
d�}
|
�|| g� W d   � n	1 �s{w   Y  |�|�� ��d� |��|��}"|�|"d��}#t|#jj�}$t d|$� �� |$|k�r�t d|� d�� t�  t�  d}%|D ]�}t|�t|d �k�rZt|d �t|�k�rZz2|%d7 }%|d d k�r�t �� d!�� �� W �q�|�
j�||d g�� t |%� d"�� ��| � W �q� � �y& }& z|�|�� ��d� W Y d }&~&�q�d }&~&w �	j�yG }' z|'jj}(t |%� d#|(� �� W Y d }'~'�q�d }'~'w   ���  t �� d$�� �� Y �q��q�|d7 }qc��d� d S )%Nz*Enter Delay Time Per Request 0 For None : r�   r   �2   r�  re   rf   rg   ri   rc   rj   r   r�  r�   r:   r�   r�   zsome thing has changedzEnter the code: r�  r  r0   r�   r�   r  r%   r�   r�  z	Members: zThe Goal Of z Has Been Completedr	   zno username, moving to nextz - doner�  r�  �r   rH   rI   rE   rN   rF   rC   rs   r�   rG   r�   r�   rI  rJ  r.   r�  ro   rD   r   r�  r�  r�  r�  r�  rn  r�  r�  r�  r�  ru   �)r�   r�   Zrexlinkr�   r�  r�  r�  r�  r�  r�  rs   r�   r�  r�  r]   r^   r�  r�   rZ   r�  r6   r�   rV   rQ   rR   rS   rT   r�  r�  r�  r�  r�  r�  r�  r�  r�  Zrexprodeltanoobr�  r  r:  r,  )r}  r   rm  r�   r�   r   r*   r?   r�  r|  r�   r�  r�  r   rn   r\   r%   r.   r�  r�  r   r�  r,   r�  r   r   r�  8  s�   
�


���	��

,
� ��
zadderforphone.<locals>.autosc            )         s�  t �j�j d � tt� �} d}t��}t��}t��d }t��}td�}td�d }t��}tdddd��}	�j|	d	d
d�}
|
�||| g� W d   � n1 sTw   Y  d}d}�||� D �]}|d7 }t d|� �� ��	|�}t d|� �� �d|� �dd�}|�
�  |�� s�t �� d�� �� |�|� |�|td�� |}g }t|dd��;}�j|d	d
d�}t|d � |D ]#}i }|d |d< |d |d< t|d �|d< |d |d< |�|� q�W d   � n1 s�w   Y  tdd��}�|�}t|�}d}d}||d  |d  }W d   � n	1 �sw   Y  t|�}|| }tdd��}�|�}t|�}d}d}||d  |d  }W d   � n	1 �sLw   Y  t|�}|| } tdddd��}!�j|!d	d
d�}
|
�|| g� W d   � n	1 �s{w   Y  |�|�� ��d� |��|��}"|�|"d��}#t|#jj�}$t d|$� �� |$|k�r�t d|� d�� t�  t�  d}%|D ]�}t|�t|d �k�rat|d �t|�k�rat d|$� �� z2|%d7 }%|d d k�r�t �� d!�� �� W �q�|�
j�||d g�� t |%� d"�� ��| � W �q� � �y- }& z|�|�� ��d� W Y d }&~&�q�d }&~&w �	j�yN }' z|'jj}(t |%� d#|(� �� W Y d }'~'�q�d }'~'w   ���  t �� d$�� �� Y �q��q�|d7 }qc��d� d S )%Nr�  r�   r   r  r�  re   rf   rg   ri   rc   rj   r   r�  r9   r:   r�   r�   u   bir şeyler ters gittirC  r�  r  r0   r�   r�   r  r%   r�   r�  r�  r�  r�  r	   r�  u    - başarılır�  zbeklenmedik hata.r  r  )r}  r   rm  r@  r�   r   r*   r?   r�  r|  r�   r�  r�  r   rn   r\   r%   r.   r�  r�  r   r�  r,   r�  r   r   �private�  s�   
�


���	��

,
� ��
zadderforphone.<locals>.privateu*   Gizli Grup İse Y Değilse N basınız. : r�   r�   )<r=   r*   r  rl  rm  r�   rn  r?   r   r�   rG  rj  r@  r�   r�  r�  r�   r�   r�  r�  r}  r�  r>   r�   r,   r|  r�   r@   r�  r�  ra   r�  rn   r�  r.   r�  r�  rA   r   r   r   r   r�  rI   rL   r�  rM   r   r   rB   r!  r"  rC   r�  ro   rE   r   rF   r�   rN   )!rl  rn  rj  r�   r�  r�  r�   r�  r�  r�  r�   r@   r�  r�  ra   r�  r�  r   r   r�  r�  r�  rA   r   r1  r]   r�  rQ   r�  r�  r�  r   Z	rexchooser   )r}  r   rm  r@  r�   r�   r   r*   r?   r�  r|  r�   r�  r�  r   rn   r\   r%   r.   r�  r�  r   r�  r,   r�  r   �adderforphone�  sp   
��(::yy



�r!  c                  C   s�   dd l } dd l}ddlm}m}m} dd l}dd l}t�  tdddd��}|j	|ddd	�}|�
g d
�� W d   � n1 s>w   Y  ttd��d }	d}
|
|	krf| jd| jd� |
d }
|�d� |
|	ksQ|�d� t�d� d S )Nr   r   r�  re   rf   rg   ri   rc   rj   �r   r   r  �/   Kaç tane hesap çalıştırmak istiyorsun? => r   zpython v1-1.py�Zcreationflagsr�   r�  )r�   rA   r   r   r   r   r?   rB   rC   rs   r�   rE   rN   �Popen�CREATE_NEW_CONSOLEr   rn   ru   �r�   rA   r   r   r   r   r?   r�  rs   r�   r~   r   r   r   �multipleadder/  s&   �
�
r(  c            #         sR  dd l } ddl m�m}m� | jdd� t�  ddlm� ddlm	� ddl
m} ddlm}m}m}m} dd	lm�m�	m}m� dd
lm} ddlm}	m}
 ddlm� ddlm}m�m� dd l}dd l }ddl!m"} dd l#�
ddl#m$} dd l%�dd l&�dd l'�dd l } ddl m�m}m� | jdd� ddl(m)} t*�j+�j, d � t-t.� �}t/dd��}||�}t0|�}|}d}||d  |d  }W d   � n1 s�w   Y  d}|d7 }t/dd��!}�
�$|�}t0|�}t-|�}d}||d  |d  }W d   � n	1 �sw   Y  t/dd��!}�
�$|�}t0|�}t-|�}d}||d  |d  }W d   � n	1 �s6w   Y  t-|�� t1|��g }t/dd��}||�}t2|�}|D ]} |�3t-| d �� �qUW d   � n	1 �smw   Y  |�|�4� }!|!�5d� |!d d �|�|!d d �� ���������	�
���������fdd�}"|"�  d S )Nr   r   Tr   r)   )r   ri  r�  r�  r�  r�  rA  r�  )�Messager-   r�  r  r1   r%   r   r/   r0   r�   r�   ro  ZMessage_filec                     s�  �} �}�� ��}�d|� �� ��}|��  |�� sJz|�|� |�|td�� td� |�|� W n �yI   td�}td� |j|d� Y nw |�� }|jsU|j	}n|j	d |j }d}g }t
|dd	��;}	�
j|	d
dd�}
t|
d � |
D ]#}i }|d |d< |d |d< t|d �|d< |d |d< |�|� qwW d   � n1 s�w   Y  ttd��}ttd��}d}|D �] }t|�t|d �k�r�t|d �t|�k�r�zQ|d7 }d}|�|d �}|d dkr�td� W q��s�|�|d|d � d|� �� n|�|�� |�|d|d � d|� �� �j�j d }����dd�� W np �	�y0   d}Y ne ��y;   d}Y nZ ��yO } zd}W Y d }~nJd }~w ��yq } z|j}td|� d �� ��|� W Y d }~n(d }~w �j�y� } z
|jj}W Y d }~nd }~w   ���  td!� Y q�t�j�j d|� d�j�j � d"�j� d�j�j � d#|d � d$|� d$|� � � q�t|d �t|�k�r�t�j�j d% � t�  t�  q�d S )&Nr:   rC  r	   rD  rE  r�   r�   rf   rg   ri   rc   rj   r   r�  r   r  r0   r�   r�   r  u   Başlangıç = u	   Bitiş = r�   r�  zMerhaba z
 r�   �   ZPrivacyRestrictedErroru   Bu Üye Zaten Grupta!r	  z saniye bekle!zBeklenmedik Hata!u    > Gönderiyor r
  r  u,   
Mesaj Gönderimi Başarıyla Tamamlandı!!
)rG   r�   r�   rI  rJ  rN   r   r  rU  r*  rC   r.   r�  rE   ro   r�  r�   Z	send_filerH   rI   r   r  r  r�  r�  r�  r�  rL   r�   r  r&   )r  ZLegend_dev_messager]   r^   rF  r�   r  r�  r�   rZ   r�  r6   r�  r�  r�  r,  Zreceiverr  r  r  r:  �r3  r   r   r4  r�  rB  r   r*   r�  r�  r?   r|  Z
legendfileZmessagessssr\   r   r   r  r�  r,   r   r   r�  �  s�   

�
��
,���V��zsendmessage.<locals>.autos)6rA   r   r   r   r   rB   r=   r*   r�   r   rG  rj  r   r�   r�  r�  r�   r�  r�  r}  r�  r  rn  rm  r�   rH  rB  r>   r�   r,   r|  r@   r   r   r)  r?   r.   r�  r   r   r�  r�  r   rH   rM   rE   rN   rC   rD   rF   r�  ro   r!  r"  )#rA   r   rj  r�   r�  r�  r�   r}  rn  rm  r�   r�   r@   r   r)  r.   r�  r  r  rQ   rR   rS   rT   r  rO   rP   rU   rV   rW   r]   r�  r�  r�  r1  r�  r   r+  r   �sendmessageB  s�   
�
�
�	��
2
Zr,  c                  C   s�   dd l } dd l}ddlm}m}m} dd l}dd l}|jdd� t�  t	dddd��}|j
|d	d
d�}|�g d�� W d   � n1 sDw   Y  ttd��d }	d}
|
|	krl| jd| jd� |
d }
|�d� |
|	ksW|�d� t�d� d S )Nr   r   Tr   r�  re   rf   rg   ri   rc   rj   r"  r#  r   zpython v1-2.pyr$  r�   r�  )r�   rA   r   r   r   r   r?   r   rB   rC   rs   r�   rE   rN   r%  r&  r   rn   ru   r'  r   r   r   �multisender�  s(   �
�
r-  c               
   C   s(  dd l } | jdd� t�  ddlm} dd l}ddlm} ddlm	} ddlm
} dd l}ddl m}m} dd l}	d	}
td
d���}dd� |�|�D �}d}|D ]�}|�|�}|d7 }t|j|j |� d� � |d|� �dd�}|�|� 	 zttd��}W q� ty�   td� Y nw qv|dkr�t�  |dkr�td�}td�}||||d�� |	�|�dd�� ||g}|�|� d�|�tt|dd � �|�dd� � }||jj |d�� |�!� }t|j|j d  |j |j" |j# � td!� d}
qOW d   � n	1 �sw   Y  t|
�rd"� d S d#� d S )$Nr   Tr   )�UpdateProfileRequestr�  r)   r+   r�   Fr1   r%   c                 S   r2   r3   r   r4   r   r   r   r7   	  r8   zupdateprof.<locals>.<listcomp>r   u    Değiştiriliyor!r:   r�  r�  u\   Ad-Soyad Değiştirmek İçin 1 / Bu Hesabı Geçmek İçin 2 / Çıkış Yapmak İçin 3: 'u   Geçersiz Giriş..r�   u   İsim : z
Soyisim : )r*  rU  r�   r*  r	   �   �d   i�  )r  u   Senin Yeni Kullanıcı Adın : u1   profil başarılı bir şekilde değiştirildi! 
r�   r;   )$rA   r   rB   Ztelethon.tl.functions.accountr.  r   r>   r�   r=   r*   r,   r?   r   r   r   rC   r.   rG   r   rH   rI   rJ   rE   rN   r~  r&   r   ZrandintZshuffle�joinrF   ZaccountZUpdateUsernameRequestr  r�   r  )rA   r.  r   r�   r*   r,   r?   r   r   r   r_   rZ   r[   rO   r\   r]   r^   Zchange_namer*  rU  r  r  r�   r   r   r   �
updateprof�  sh   

���
*�&��)r2  z
./sessionsr1   re   r0   r�   r�   r�   r*  �   r/  �	   r�  �   �   �   �   r  �   �   �   �   �   �   �   )Ern   r   r   rA   r   r   r   r   r@   rL   r   ZLIGHTGREEN_EXZlgr�   r%   ZWHITEre   r  ZcyrM   r�  r   r   r   r�   r�   rF   Zcheck_outputr#  rp   r$  r$   �getr"   r'   r�  r   rH   ZLIGHTCYAN_EXrE   rN   Z#This_is_normal_script_by_legend_devr`   r�   r�   r>  rK  rf  rg  r�  r�  r�  r�  rB   r�  r�  r�  r�  r  r!  r(  r,  r-  r2  �path�exists�mkdirrC   r&   r   r   r   r   �<module>   s   ,
1 r 0   / =
2oY! /  9 )
9













































�0