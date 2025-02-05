import os
from pathlib import Path

import click

from common.download import download_tiles_s3
from common.process import process_scene

@click.command()
@click.option("--event_name", default=None, help="STAC Event Name.")
@click.option("--scene_id", default=None, help="CATID of the MAXAR scene.")
@click.option("--output_name", default="out.tif", help="Output TIFF name.")
def main(event_name, scene_id, output_name):

    Path(f"SCENES/{scene_id}").mkdir(parents=True, exist_ok=True)
    download_path = Path(f"SCENES/{scene_id}")  

    download_tiles_s3(
        event_name=event_name,
        scene_id=scene_id,
        download_path=download_path,
    )

    output_path = Path(
        f"SCENES/{scene_id}/{output_name}"
    )

    process_scene(scene_path=download_path, output_path=output_path)

if __name__ == '__main__':
    main()