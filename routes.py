from flask import Blueprint, send_file, abort
from CTFd.utils.decorators import authed_only
from CTFd.utils.user import get_current_user
from CTFd.utils.user import get_current_team
#from CTFd.utils.user import get_solve_count
from CTFd.models import Solves
from PIL import Image, ImageDraw, ImageFont
import tempfile
import os
import time

certificates = Blueprint("certificates", __name__)

BASE_DIR = os.path.dirname(__file__)
CERT_TEMPLATE = os.path.join(BASE_DIR, "cert.png")
FONT_PATH = "/usr/share/fonts/truetype/dejavu/Silentha.ttf"
CERT_LOG_DIR = "/var/log/certificates"

FONT_SIZE = 200
FONT_COLOR = "white"
Y_POSITION = 1052

def log_certificate_generation(user, team):
    os.makedirs(CERT_LOG_DIR, exist_ok=True)

    user_id = user.id
    username = user.name.replace(",", "_")
    teamname = team.name.replace(",", "_") if team else ""
    current_time = time.ctime()

    filepath = os.path.join(CERT_LOG_DIR, f"user_{user_id}.txt")

    # If file already exists, do nothing (idempotent)
    if os.path.exists(filepath):
        return

    line = f'{current_time},{username},{teamname},"success"\n'

    # Atomic file creation
    with open(filepath, "x", encoding="utf-8") as f:
        f.write(line)

@certificates.route("/certificates/download")
@authed_only
def download_certificate():
    user = get_current_user()
    team = get_current_team()

    if not user:
        abort(403)

    if user:
        solves = Solves.query.filter_by(user_id=user.id).count()
        if solves == 0:
            abort(403, "You need to have solved at least one challenge to get a certificate")

    try:
        username = user.name.strip()+" of Team "+team.name.strip()

        img = Image.open(CERT_TEMPLATE).convert("RGBA")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

        x_center = img.width // 2

        draw.text(
            (x_center, Y_POSITION),
            username,
            fill=FONT_COLOR,
            font=font,
            anchor="mm"
        )

        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        img.save(tmp.name)
        tmp.close()

        log_certificate_generation(get_current_user(),get_current_team())

        return send_file(
            tmp.name,
            mimetype="image/png",
            as_attachment=True,
            download_name=f"{username}_certificate.png"
        )

        

    except Exception as e:
        abort(500)

