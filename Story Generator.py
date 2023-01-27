from asyncio import run

from Mules.NovelAI_SignIn import API

from novelai_api.ImagePreset import ImageModel, ImagePreset, ImageResolution, UCPreset, ImageSampler
import random

async def main():
    async with API() as api_handler:
        api = api_handler.api

        ####   Meesh variables

        # Select model, either Anime_Full Anime_Curated or Furry (Anime_Curated seems to be less sexual)
        my_model = ImageModel.Anime_Curated

        pages = [ # [The characters for this scene, what the characters are doing, the context for the scene]
                      ["three Bears standing in a forest", "the bears are looking around" , "Once upon a time, there were three hungry bears living in the forest. Brother Bear was the oldest of the three, and he was always searching for food."]
                    , ["One Bear standing in a forest", "the bear is looking at a beehive up high in a tree with bees flying around it. The scene is peaceful" , "One day Brother Bear spotted a bee hive full of honey. He thought to himself that he could just take some of it without anyone knowing, but then he reminded himself that stealing isn't right. "]
                    , ["One Bear standing in a forest", "The bear has climbed a tree up to a beehive, honey is dripping out", "So instead, Brother Bear decided to build a tall ladder and use it to reach the top of the tree so he could patiently wait for an opportunity to get some honey - but not too much."]
                    , ["One Bear standing in a forest", "The bear is looking a a briar patch or berry patch", "Meanwhile, Sister Bear had found a patch of wild berries nearby and she was tempted to take them all. But after remembering her brother's words about stealing, she decided it was best to only take what she needed. "]
                    , ["One Bear standing in a campground", "The bear is looking at a picnic basket", "The youngest bear, Baby Bear had discovered an abandoned picnic basket full of delicious treats! But even though no one was around, Baby Bear remembered his siblings' words about stealing being wrong and chose only to take enough for himself and his family. "]
                    , ["Three Bears standing together in a forest", "One bear is holding a berry, one bear has honey on their face, the last bear is holding a sandwhich", "The three bears quickly realized that there are more ways than stealing to get food in the forest! And so they banded together in search of more sustainable sources like fishing streams or berry patches where they could forage for food without taking too much. "]
                    , ["Three Bears walking along a stream", "Three bears walking in a line by a stream in a forest","By following this moral code that stealing is wrong, the bears learned how to live peacefully in their forest home; never taking more than their fair share from any single source and helping each other when one bear was in need. " ]
                    , ["Three bears laying on the ground", "The three bears on the top of a hill are laying on their backs, under the stars. The bears have full bellies", "And when their bellies were full, they would often sit under the stars and talk about how bad it would be if everyone stole from each other instead of sharing what they had with kindness and generosity. "]
                    , ["Three bear faces, side by side", "The three bears are smiling at us", "The three bears learned an important lesson: That if we all work together and respect one another's boundaries, then no one needs to steal!  And so they lived happily ever after in harmony with nature and one another - never once taking more than what was theirs!"]
        ]

        #Add prefix text to all pages
        prefix = "Watercolor, black and white, childerns book style. The only characters visible are "

        #Add suffix text to all pages
        suffix = ""

        listOfRands = []
        for number in range(0,4):
            listOfRands.append(random.randint(1,0xFFFFFFFF))
        print(listOfRands)
        # multiple images

        # preset["n_samples"] = 4
        i = 4
# prefix + page1 + suffix, my_model, preset
        for page in pages:
            for rand in listOfRands:
                print(rand)
                preset = ImagePreset(
                    quality_toggle=True
                    , resolution = ImageResolution.Normal_Square
                    , uc_preset = UCPreset.Preset_Low_Quality_Bad_Anatomy
                    , n_samples = 1
                    , seed = rand
                    , sampler = ImageSampler.k_euler_ancestral
                    , noise = 0.2
                    , strength = 0.7
                    , steps = 28
                    , scale = 11
                    , uc = "" 
                    )
                async for img in api.high_level.generate_image(prefix + page[0] + ". The image shows "+ page[1]+" . The context from the story is " + page[2] + suffix, my_model, preset):
                    with open(f"img_page"+str(i)+"Seed"+str(rand)+".png", "wb") as f:
                        f.write(img)
            i += 1

                


            

run(main())
