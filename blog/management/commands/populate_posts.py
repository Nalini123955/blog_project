from typing import Any
from blog.models import Post, Category
from django.core.management.base  import BaseCommand
import random

 
class Command(BaseCommand):
    help = "This commands inserts post data"
    #delete existing data
    def handle(self, *args: Any, **options: Any):
        #Delete existing data
        Post.objects.all().delete()
        titles = [
               "Future of AI",
               "Code That Changes the World",
               "Empowering Ideas with Code",
               "The Art of Smart Software",
               "Tomorrow Begins with Code",
               "Creating Intelligence with Code",
               "Simplifying Life Through Software"
               "Beyond Limits with Logic",
               "Innovation Starts in the IDE",
               "Coding the Future Today",
               "Technology That Thinks",
               "Smart Code for a Smarter World",
               "Ideas Turned into Interfaces",
               "Logic Behind Every Click",
               "Crafting Digital Experiences",
               "From Concept to Code",
               "Solving Problems with Programs",
               "Where Creativity Meets Code",
               "Software that Shapes Tomorrow"
               "One Line of Code at a Time"
        ]
        contents = [

               "Future of AI The future of artificial intelligence lies in its ability to transcend traditional Don’t wait for the perfect moment.Start now and make every moment perfect.",
               "Advances in generative AI, such as large language models and image synthesis tools, are democratizing,You have the power to change your story.Take the pen and write your own ending",
               "Code That Changes the World Code is the invisible force driving modern civilization,Dreams don’t work unless you do.Show the world what you're made of",
               "Open-source projects like Linux powering global infrastructure to apps coordinating disaster relief efforts Even the smallest step moves you forward.Progress is better than perfection", 
               "software bridges the gap between ideas and impact. Consider how GPS navigation, built on millions of lines of code Every failure is a lesson in disguise.Stand up, learn, and shine brighter",
               "Empowering Ideas with Code Transforming an idea into functional software is akin to sculpting with logic You are capable of more than you believe.Trust yourself and take the leap",
               "problem— say, streamlining small business inventory management—and evolves through wireframes, prototypes Stop doubting. Start doing.The world needs your spark Your effort today builds your future.Keep going, you're getting closer", 
               "The Art of Smart Software Smart software thrives on elegance and efficiency. It adheres to principles like DRY Your effort today builds your future.Keep going, you're getting closer",
               "Crafting Digital Experiences The pain you feel now fuels your strength. Push through, greatness is near.",
                "Digital experiences are the new frontier of human interactio You were born to stand out. Never shrink to fit into small spaces",
                "A seamless UI/UX design—responsive layouts, accessible color contrasts, and intuitive navigation—can turn casual users into loyal advocates",
                "Imagine an e-learning platform where animationsDon’t wait for the perfect moment.Start now and make every moment perfect.",
                "Solving Problems with Programs At its core, programming is problem-solving distilled into logic",
                "Whether optimizing delivery routes using graph algorithms or detecting financial fraud through anomaly detection models", 
                "Code translates abstract challenges into actionable solutions Don’t compare your path to others.Your journey is unique and powerful.",
                "Take the binary search algorithm: a few lines of Python can locate data in logarithmic time Keep your focus, ignore the noise. Your goals deserve your full attention.", 
                "Revolutionizing database efficiency. Developers act as modern-day alchemists Be proud of how far you’ve come.\nYour journey inspires others silently",
                "Turning lines of code into tools that streamline workflows, reduce errors, and unlock new possibilities You don’t need approval to shine.\nYour light is already enough.",
                "The key is to decompose problems into modular components—each solvable, testable, and scalable Don’t give up now, you're closer than ever.\nPush harder, the finish line is nea",
                "Where Creativity Meets Code Coding is a canvas for boundless creativity You don’t need approval to shine.\nYour light is already enough",
       
        ]

        img_urls = [
                "https://picsum.photos/id/1/800/400",
                "https://picsum.photos/id/2/800/400",
                "https://picsum.photos/id/3/800/400",
                "https://picsum.photos/id/4/800/400",
                "https://picsum.photos/id/5/800/400",
                "https://picsum.photos/id/6/800/400",
                "https://picsum.photos/id/7/800/400",
                "https://picsum.photos/id/8/800/400",
                "https://picsum.photos/id/9/800/400",
                "https://picsum.photos/id/10/800/400",
                "https://picsum.photos/id/11/800/400",
                "https://picsum.photos/id/12/800/400",
                "https://picsum.photos/id/13/800/400",
                "https://picsum.photos/id/14/800/400",
                "https://picsum.photos/id/15/800/400",
                "https://picsum.photos/id/16/800/400",
                "https://picsum.photos/id/17/800/400",
                "https://picsum.photos/id/18/800/400",
                "https://picsum.photos/id/19/800/400",
                "https://picsum.photos/id/20/800/400",
        ]
        categories = Category.objects.all()
        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)
            
        self.stdout.write(self.style.SUCCESS('Completed inserting Data!'))
