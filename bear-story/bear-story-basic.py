from asyncio import run

from boilerplate import API

from novelai_api.ImagePreset import ImageModel, ImagePreset, ImageResolution, UCPreset







async def main():
    async with API() as api_handler:
        api = api_handler.api

        ####   Meesh variables

        # Select model, either Anime_Full Anime_Curated or Furry (Anime_Curated seems to be less sexual)
        my_model = ImageModel.Anime_Curated

        #Create Text For Pages
        page1 = "Once upon a time, there were three bears, two sisters and one brother. They were very hungry and wanted to find something to eat. The bears had happy faces"
        page2 = "The brother bear decided to try his luck at a nearby bee hive in hopes of finding honey. He was careful not to disturb the bees, and was rewarded with a delicious treat for himself and his siblings."
        page3 = "The two sister bears went into the woods in search of berries. After some exploring, they found some ripe blackberries and enjoyed a tasty snack."
        page4 = "Feeling still unsatisfied, the three bears came up with an idea to look for food from unsuspecting park visitors. The brother bear decided against it though, knowing that it wasn't the right thing to do."
        page5 = "The sister bears asked why he wouldn't join them, and he replied that it was wrong to take things that don't belong to you, even if you're hungry."
        page6 = "Although they were sad at first, the two sisters understood what their brother meant and agreed with him. The three bears then decided to go back home as they knew their parents would be able to provide them with more food when they arrived back home."
        page7 = "On their way back however, the three bears stumbled across an abandoned lunch basket filled with delicious snacks! This time all three bears agreed that it would be alright to take it as no one seemed like they wanted it back anymore!"
        page8 = "So with full bellies and big smiles on their faces, they went home."

        #Add prefix text to all pages
        prefix = "Watercolor art style."

        #Add suffix text to all pages
        suffix = "Children's book illustration style."




        preset = ImagePreset()

        # multiple images

        # preset["n_samples"] = 4
        i = 0

        async for img in api.high_level.generate_image(prefix + page1 + suffix, my_model, preset):
            with open(f"img_page1.png", "wb") as f:
                f.write(img)

            i += 1

        # page2
  
        
        async for img in api.high_level.generate_image(prefix + page2 + suffix, my_model, preset):
            with open(f"img_page2.png", "wb") as f:
                f.write(img)
         

        # page3

        
        async for img in api.high_level.generate_image(prefix + page3 + suffix, my_model, preset):
            with open(f"img_page3.png", "wb") as f:
                f.write(img)
           

        # page4
       
        async for img in api.high_level.generate_image(prefix + page4 + suffix, my_model, preset):
            with open(f"img_page4.png", "wb") as f:
                f.write(img)
            

        # page5
             
 
        async for img in api.high_level.generate_image(prefix + page5 + suffix, my_model, preset):
            with open(f"img_page5.png", "wb") as f:
                f.write(img)
            

        # page6

        
        async for img in api.high_level.generate_image(prefix + page6 + suffix, my_model, preset):
            with open(f"img_page6.png", "wb") as f:
                f.write(img)
           

        # page7
       
        async for img in api.high_level.generate_image(prefix + page7 + suffix, my_model, preset):
            with open(f"img_page7.png", "wb") as f:
                f.write(img)
            

        # page8
             
 
        async for img in api.high_level.generate_image(prefix + page8 + suffix, my_model, preset):
            with open(f"img_page8.png", "wb") as f:
                f.write(img)
            

run(main())
