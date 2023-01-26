from asyncio import run

from Mules.NovelAI_SignIn import API

from novelai_api.ImagePreset import ImageModel, ImagePreset, ImageResolution, UCPreset, ImageSampler


async def main():
    async with API() as api_handler:
        api = api_handler.api

        ####   Meesh variables

        # Select model, either Anime_Full Anime_Curated or Furry (Anime_Curated seems to be less sexual)
        my_model = ImageModel.Anime_Curated

        pages = {
                    # "Once upon a time, there were three bears, two sisters and one brother. They were very hungry and wanted to find something to eat. The bears had happy faces"
                    # , "The brother bear decided to try his luck at a nearby bee hive in hopes of finding honey. He was careful not to disturb the bees, and was rewarded with a delicious treat for himself and his siblings."
                    # , "The two sister bears went into the woods in search of berries. After some exploring, they found some ripe blackberries and enjoyed a tasty snack."
                    # , "Feeling still unsatisfied, the three bears came up with an idea to look for food from unsuspecting park visitors. The brother bear decided against it though, knowing that it wasn't the right thing to do."
                    # , "The sister bears asked why he wouldn't join them, and he replied that it was wrong to take things that don't belong to you, even if you're hungry."
                    # , "Although they were sad at first, the two sisters understood what their brother meant and agreed with him. The three bears then decided to go back home as they knew their parents would be able to provide them with more food when they arrived back home."
                    # , "On their way back however, the three bears stumbled across an abandoned lunch basket filled with delicious snacks! This time all three bears agreed that it would be alright to take it as no one seemed like they wanted it back anymore!"
                    "Three cute, fuzzy Bears with full bellies and big smiles on their faces, walking home. The Three Bears are in a forest. it is bright outside. the image makes you feel happy."
                }

        #Add prefix text to all pages
        prefix = "Watercolor art style."

        #Add suffix text to all pages
        suffix = "Children's book illustration style."

        preset = ImagePreset(
                quality_toggle=True
                , resolution = ImageResolution.Normal_Square
                , uc_preset = UCPreset.Preset_Low_Quality_Bad_Anatomy
                , n_samples = 1
                , seed = 99
                , sampler = ImageSampler.k_euler_ancestral
                , noise = 0.2
                , strength = 0.7
                , steps = 28
                , scale = 11
                , uc = "")

        # multiple images

        # preset["n_samples"] = 4
        i = 0
# prefix + page1 + suffix, my_model, preset
        for page in pages:
            async for img in api.high_level.generate_image(page, my_model, preset):
                with open(f"img_page"+str(i)+".png", "wb") as f:
                    f.write(img)
                i += 1

                


            

run(main())
