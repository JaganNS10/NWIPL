from django.db import migrations

SEED = [
    ("NWI-BC-1A-01", "The same precision-engineered frame as NWI-BC-1A, fitted with locking wheel castors for easy repositioning — ideal for nurseries and hospitals that need mobility without compromising structural strength.",
     "Engineered MDF core with solid wood framing", "Non-toxic, child-safe paint", "With locking wheel castors", "images/BabyCot/nwibc1a01.jpeg"),
    ("NWI-BC-1A-02", "Our arched-headboard design — a classic silhouette with a curved top rail, finished in the same child-safe, non-toxic paint standard as every NWI-BC model. Fixed-leg variant.",
     "Engineered MDF core with solid wood framing", "Non-toxic, child-safe paint", "Fixed legs", "images/BabyCot/nwibc1a02.jpeg"),
    ("NWI-BC-1A-03", "The arched-headboard design fitted with locking wheel castors — combining classic styling with the mobility needed for busy nurseries.",
     "Engineered MDF core with solid wood framing", "Non-toxic, child-safe paint", "With locking wheel castors", "images/BabyCot/nwibc1a03.jpeg"),
    ("NWI-BC-1A-04", "Our modern design — solid rubber wood grain end panels paired with grey-painted slat side rails, fitted with locking wheel castors. A contemporary alternative to our classic slatted range.",
     "MDF + Rubber Wood", "Grey paint", "With locking wheel castors", "images/BabyCot/nwibc1a04.jpeg"),
]


def seed(apps, schema_editor):
    Model = apps.get_model("app", "BabyCotModel")
    for i, (code, desc, material, finish, variant, image) in enumerate(SEED, start=1):
        Model.objects.get_or_create(code=code, defaults=dict(
            description=desc, material=material, finish=finish,
            joinery="Dowel & barrel-nut construction", variant=variant, image=image, position=i,
        ))


def unseed(apps, schema_editor):
    apps.get_model("app", "BabyCotModel").objects.filter(code__in=[s[0] for s in SEED]).delete()


class Migration(migrations.Migration):
    dependencies = [("app", "0002_enquiry_and_cot")]
    operations = [migrations.RunPython(seed, unseed)]
