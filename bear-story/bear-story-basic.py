from asyncio import run

from boilerplate import API

from novelai_api.ImagePreset import ImageModel, ImagePreset, ImageResolution, UCPreset


async def main():
    async with API() as api_handler:
        api = api_handler.api

        preset = ImagePreset()

        # multiple images

        # preset["n_samples"] = 4
        i = 0

        async for img in api.high_level.generate_image("Watercolor art style. Once upon a time, there were three bears, two sisters and one brother. They were very hungry and wanted to find something to eat. The bears had happy faces", ImageModel.Anime_Full, preset):
            with open(f"INO_image_01_{i}.png", "wb") as f:
                f.write(img)

            i += 1

        # page2
  
        
        async for img in api.high_level.generate_image("Watercolor art style. The brother bear decided to try his luck at a nearby bee hive in hopes of finding honey. He was careful not to disturb the bees, and was rewarded with a delicious treat for himself and his siblings. The bees had cute faces and the bears were happy.", ImageModel.Anime_Full, preset):
            with open(f"INO_image_02_{i}.png", "wb") as f:
                f.write(img)
         

        # page3

        
        async for img in api.high_level.generate_image("Watercolor art style. The two sister bears went into the woods in search of berries. After some exploring, they found some ripe blackberries and enjoyed a tasty snack. The sister bears were very happy to eat berries.", ImageModel.Anime_Full, preset):
            with open(f"INO_image_03_{i}.png", "wb") as f:
                f.write(img)
           

        # page4
       
        async for img in api.high_level.generate_image("Watercolor art style. Feeling still unsatisfied, the three bears came up with an idea to look for food from unsuspecting park visitors. The brother bear decided against it though, knowing that it wasn't the right thing to do.", ImageModel.Anime_Full, preset):
            with open(f"INO_image_04_{i}.png", "wb") as f:
                f.write(img)
            

        # page5
             
 
        async for img in api.high_level.generate_image("Watercolor art style. The sister bears asked why he wouldn't join them, and he replied that it was wrong to take things that don't belong to you, even if you're hungry.", ImageModel.Anime_Full, preset):
            with open(f"INO_image_05_{i}.png", "wb") as f:
                f.write(img)
            

run(main())
