<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Entry: Wood & Platforms</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Georgia&family=Impact&display=swap');
        body {
            font-family: 'Georgia', serif;
            background: url('https://via.placeholder.com/1600x900?text=Rural+Landscape') center/cover fixed;
            color: #ddd;
            padding: 40px;
            line-height: 1.6;
            position: relative;
            overflow-x: hidden;
        }
        /* faint wood grain overlay */
        body::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: url('https://via.placeholder.com/800x800?text=Wood+Grain') center/contain repeat;
            opacity: 0.15;
            pointer-events: none;
            mix-blend-mode: overlay;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: rgba(0,0,0,0.6);
            padding: 40px;
            border-radius: 0;
        }
        h1 {
            text-align: center;
            color: #fff;
            font-family: 'Impact', sans-serif;
            font-size: 3rem;
            letter-spacing: 2px;
            text-transform: uppercase;
        }
        h2 {
            color: #ccc;
            margin-top: 30px;
            font-family: 'Impact', sans-serif;
            font-size: 2rem;
            text-transform: uppercase;
        }
        p, blockquote {
            font-size: 1.1rem;
            color: #eee;
        }
        .wood-image {
            display: block;
            margin: 20px auto;
            max-width: 100%;
            height: auto;
            filter: blur(2px) brightness(0.8);
        }
        blockquote {
            margin: 20px 0;
            padding: 15px 20px;
            background: rgba(50,50,50,0.5);
            border-left: 5px solid #aaa;
            font-style: italic;
        }
        .platform {
            background: rgba(80,80,80,0.5);
            padding: 15px;
            margin: 20px 0;
        }
        .platform h3 {
            margin-top: 0;
            font-family: 'Impact', sans-serif;
        }
        /* surveillance scanline effect */
        #scanlines {
            position: fixed;
            top:0; left:0; width:100%; height:100%;
            pointer-events:none;
            background: linear-gradient(rgba(255,255,255,0.05) 50%, transparent 50%) repeat;
            background-size: 100% 4px;
            animation: scan 5s linear infinite;
            mix-blend-mode: screen;
        }
        @keyframes scan {
            from {background-position: 0 0;}
            to {background-position: 0 100%;}
        }
    </style>
</head>
<body>
    <div class="bg"></div>
    <div class="container">
        <div class="text-block" aria-label="csv terracotta data">
            <!-- imagine a subsite of terracotta CSV data exists here -->
        </div>
    </div>
    <!-- audio plays automatically; mute if needed -->
    <audio src="csv/star-wars-theme.ogg" autoplay loop></audio>
    <style>
        body { margin:0; padding:0; overflow:hidden; font-family: 'Impact', 'Arial Black', sans-serif; color:#fff; }
        .bg {
            position:fixed; top:0; left:0; width:100vw; height:100vh;
            background: url('csv/utah-monolith.jpg') center/cover no-repeat;
            filter: saturate(0.6) contrast(1.2) brightness(0.4);
        }
        .container {
            position: relative;
            width:100%; height:100%;
            display:flex; flex-direction:column; justify-content:center; align-items:center;
            text-align:center;
            backdrop-filter: blur(4px);
        }
        .text-block {
            width: 60%;
            height: 20%;
            background: rgba(30,20,10,0.5); /* terracotta-ish shade */
            backdrop-filter: blur(2px);
            border: 2px solid rgba(255,255,255,0.2);
            position: relative;
        }
        .text-block::before {
            content: '';
            position: absolute;
            top:0; left:0; right:0; bottom:0;
            background: repeating-linear-gradient(45deg,
                rgba(204,138,100,0.6) 0,
                rgba(204,138,100,0.6) 10px,
                rgba(224,160,128,0.6) 10px,
                rgba(224,160,128,0.6) 20px);
            pointer-events: none;
            mix-blend-mode: multiply;
        }
        /* headings removed since text is gone */
    </style>
</body>
</html>
