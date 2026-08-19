from django.http import HttpResponse

def home(request):
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asadbek - Portfolio</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
</head>
<body class="bg-[#0b0d10]">
    <nav class="fixed top-[0px] left-[0px] w-[100%] z-[50] bg-[#0b0d10] border-b-[1px] border-[#1e2126] px-[24px] py-[16px] flex justify-between items-center">
        <a href="#" class="text-[20px] font-bold tracking-tight">
            <span class="bg-gradient-to-r from-[#60a5fa] to-[#a78bfa] to-[#f472b6] bg-clip-text text-transparent">Asadbek</span>
        </a>
        <div class="hidden md:flex items-center text-[14px] text-[#9ca3af]">
            <a href="#about" class="mx-[16px]">About</a>
            <a href="#skills" class="mx-[16px]">Skills</a>
            <a href="#projects" class="mx-[16px]">Projects</a>
            <a href="#experience" class="mx-[16px]">Experience</a>
            <a href="#contact" class="mx-[16px]">Contact</a>
        </div>
        <button id="menuToggle" class="md:hidden text-[#9ca3af] text-[20px]">
            <i class="bi bi-list"></i>
        </button>
    </nav>
    <div id="mobileMenu" class="md:hidden hidden bg-[#0b0d10] border-b-[1px] border-[#1e2126] px-[24px] py-[16px] fixed top-[72px] left-[0px] w-[100%] z-[40]">
        <a href="#about" class="block text-[14px] text-[#9ca3af] py-[10px]">About</a>
        <a href="#skills" class="block text-[14px] text-[#9ca3af] py-[10px]">Skills</a>
        <a href="#projects" class="block text-[14px] text-[#9ca3af] py-[10px]">Projects</a>
        <a href="#experience" class="block text-[14px] text-[#9ca3af] py-[10px]">Experience</a>
        <a href="#contact" class="block text-[14px] text-[#9ca3af] py-[10px]">Contact</a>
    </div>
    <section id="home" class="min-h-[100vh] flex items-center justify-center px-[24px] pt-[100px] pb-[60px]">
        <div class="max-w-[900px] mx-auto text-center">
            <div class="inline-flex items-center bg-[#1a1e24] border-[1px] border-[#2a2e36] rounded-[99px] px-[16px] py-[6px] text-[13px] text-[#9ca3af] mb-[24px]">
                <span class="w-[8px] h-[8px] bg-[#34d399] rounded-[50%] inline-block mr-[8px]"></span>
                Open to opportunities
            </div>
            <h1 class="text-[32px] md:text-[68px] font-bold leading-[1.15] tracking-tight text-[#e8edf5]">
                I'm <span class="bg-gradient-to-r from-[#60a5fa] to-[#a78bfa] to-[#f472b6] bg-clip-text text-transparent">Asadbek</span>
            </h1>
            <p class="text-[18px] md:text-[26px] text-[#9ca3af] mt-[16px] max-w-[600px] mx-auto">
                Web App Developer &nbsp;·&nbsp; Full‑Stack Enthusiast
            </p>
            <div class="flex flex-wrap justify-center mt-[32px]">
                <a href="#projects" class="bg-gradient-to-r from-[#60a5fa] to-[#7c3aed] rounded-[99px] px-[32px] py-[14px] font-semibold text-[#fff] text-[16px] inline-block mx-[8px] mb-[12px]">View work</a>
                <a href="#contact" class="border-[1.5px] border-[#2a2e36] rounded-[99px] px-[32px] py-[14px] font-medium text-[#e8edf5] text-[16px] inline-block mx-[8px] mb-[12px]">Let's talk</a>
            </div>
            <div class="flex justify-center mt-[40px]">
                <a href="#" class="text-[#6b7280] text-[22px] mx-[12px]"><i class="bi bi-github"></i></a>
                <a href="#" class="text-[#6b7280] text-[22px] mx-[12px]"><i class="bi bi-linkedin"></i></a>
                <a href="#" class="text-[#6b7280] text-[22px] mx-[12px]"><i class="bi bi-twitter-x"></i></a>
                <a href="#" class="text-[#6b7280] text-[22px] mx-[12px]"><i class="bi bi-dev"></i></a>
            </div>
        </div>
    </section>
    <!-- Continue with the rest of your HTML content -->
    <section id="about" class="px-[24px] py-[80px] max-w-[1100px] mx-auto">
        <!-- About section content -->
    </section>
    <section id="skills" class="px-[24px] py-[80px] bg-[#0f1116]">
        <!-- Skills section content -->
    </section>
    <section id="projects" class="px-[24px] py-[80px] max-w-[1100px] mx-auto">
        <!-- Projects section content -->
    </section>
    <section id="experience" class="px-[24px] py-[80px] bg-[#0f1116]">
        <!-- Experience section content -->
    </section>
    <section id="contact" class="px-[24px] py-[80px] max-w-[1100px] mx-auto">
        <!-- Contact section content -->
    </section>
    <footer class="border-t-[1px] border-[#1e2126] px-[24px] py-[32px] text-center text-[14px] text-[#6b7280] bg-[#0b0d10]">
        <div class="max-w-[1100px] mx-auto flex flex-col md:flex-row justify-between items-center">
            <p class="mb-[12px] md:mb-[0px]">© 2026 Asadbek Abdulhamidov. Built with <i class="bi bi-heart-fill text-[#60a5fa]"></i> &amp; TailwindCSS</p>
            <div class="flex">
                <a href="#" class="text-[#6b7280] mx-[12px]"><i class="bi bi-github"></i></a>
                <a href="#" class="text-[#6b7280] mx-[12px]"><i class="bi bi-linkedin"></i></a>
                <a href="#" class="text-[#6b7280] mx-[12px]"><i class="bi bi-twitter-x"></i></a>
                <a href="#" class="text-[#6b7280] mx-[12px]"><i class="bi bi-dev"></i></a>
            </div>
        </div>
    </footer>
    <script>
        var menuToggle = document.getElementById('menuToggle');
        var mobileMenu = document.getElementById('mobileMenu');
        menuToggle.addEventListener('click', function() {
            if (mobileMenu.classList.contains('hidden')) {
                mobileMenu.classList.remove('hidden');
            } else {
                mobileMenu.classList.add('hidden');
            }
        });
        document.querySelectorAll('#mobileMenu a').forEach(function(link) {
            link.addEventListener('click', function() {
                 mobileMenu.classList.add('hidden');
            });
        });
        var form = document.getElementById('contactForm');
        var status = document.getElementById('formStatus');
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            status.innerHTML = '<span class="text-[#60a5fa]"><i class="bi bi-arrow-repeat bi-spin mr-[6px]"></i> Sending…</span>';
            setTimeout(function() {
                status.innerHTML = '<span class="text-[#34d399]"><i class="bi bi-check-circle mr-[6px]"></i> Message sent! I\'ll get back to you soon.</span>';
                form.reset();
            }, 1200);
        });
        document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
            anchor.addEventListener('click', function(e) {
                var targetId = this.getAttribute('href');
                if (targetId === '#') return;
                var target = document.querySelector(targetId);
                if (target) {
                    e.preventDefault();
                    var navHeight = 72;
                    var top = target.getBoundingClientRect().top + window.scrollY - navHeight;
                    window.scrollTo({ top: top, behavior: 'smooth' });
                }
            });
        });
    </script>
</body>
</html>"""
    return HttpResponse(html_content)