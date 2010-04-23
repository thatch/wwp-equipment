__all__ = ["rules"]

rules = [
    [
    # Canon
    (r'EOS-1D Mark IIN', ('camera', 'Canon-1DmarkIIN')),
    (r'EOS-1D Mark II', ('camera', 'Canon-1DmarkII')),
    (r'1DS ?mk(3|III)', ('camera', 'Canon-1DSmark3')),
    (r'1DS ?mkII|Canon 1ds2|1DS MII', ('camera', 'Canon-1DSmark2')),
    (r'(Canon|EOS).*1DS', ('camera', 'Canon-1DS')),
    (r'Canon 1D MarkII', ('camera', 'Canon-1Dmark2')), #JacquesJoffre
    (r'Can+on.*5 *D(?!X)|EOS 5D', ('camera', 'Canon-5D')),
    (r'Canon.*\b6D', ('camera', 'Canon-6D')),
    (r'Canon.*\b7D', ('camera', 'Canon-7D')),
    (r'Canon.*\b10D|EOS *10D|Canon10D', ('camera', 'Canon-10D')),
    (r'Canon.*\b20D|EOS *20D|\b20D|Canon20D', ('camera', 'Canon-20D')),
    (r'Canon.*\b30D|EOS *30D|Canon30D', ('camera', 'Canon-30D')),
    (r'Canon.*\b40D|EOS *40D|Canon40D', ('camera', 'Canon-40D')),
    (r'(Canon|EOS).*\b50D', ('camera', 'Canon-50D')),
    (r'Canon D30', ('camera', 'Canon-D30')),
    (r'Canon D60', ('camera', 'Canon-D60')),
    (r'Canon D40', ('camera', 'Canon-40D')), #RussAddie
    (r'450D|Canon 450|rebel xsi', ('camera', 'Canon-450D')),
    (r'400D|kiss.*digital.*xti|rebel.*xti|canon.*xti|kiss\s*dn', ('camera', 'Canon-400D')),
    (r'EOS 350|350 *D|350XT|kiss.*digital|rebel.*xt', ('camera', 'Canon-350D')),
    (r'300D(?!X)|digital.*eos|digital.*rebel|eos.*digital', ('camera', 'Canon-300D')),
    (r'Canon.*500D', ('camera', 'Canon-500D')),
    (r'EOS[ -]600', ('camera', 'Canon-EOS600')), #FIXME: keep EOS?
    (r'Canon Pro1|PowerShot Pro 1', ('camera', 'Canon-PowershotPro1')),
    (r'Canon EOS500N', ('camera', 'Canon-EOS500n')),
    (r'Canon A640', ('camera', 'Canon-A640')),
    (r'(?!<=\.)\b5D(?!X)', ('camera', 'Canon-5D')), #RichardCambon, HiroharuShizuya
    (r'Canon (?:EOS )?1000D', ('camera', 'Canon-1000D')),

    # Canon neat things but not SLR
    (r'Canon G6', ('camera', 'Canon-G6')),
    (r'Canon G7', ('camera', 'Canon-G7')),
    (r'Canon G8', ('camera', 'Canon-G8')),
    (r'PowerShot G9', ('camera', 'Canon-G9')),

    # Nikon
    (r'Nikon\s*D3\b', ('camera', 'Nikon-D3')),
    (r'Nikon\s*D3x\b', ('camera', 'Nikon-D3x')),
    (r'Nikon.*(?:D-?70s|70DS)', ('camera', 'Nikon-D70s')), # Same as next?
    (r'Nikon.*D-?70\b', ('camera', 'Nikon-D70')),
    (r'Nikon.*D80', ('camera', 'Nikon-D80')),
    (r'Nikon.*D90', ('camera', 'Nikon-D90')),
    (r'Nikon.*D *100', ('camera', 'Nikon-D100')),
    (r'Nikon.*D *200', ('camera', 'Nikon-D200')),
    (r'Nikon.*D *300', ('camera', 'Nikon-D300')),
    (r'^\s*D300', ('camera', 'Nikon-D300')), #WS req due to AndreyKharuk in 308 (ZW S, BOM?)
    (r'Nikon.*D *400', ('camera', 'Nikon-D400')),
    (r'Nikon.*D *500', ('camera', 'Nikon-D500')),
    (r'Nikon.*D *600', ('camera', 'Nikon-D600')),
    (r'Nikon.*D *700', ('camera', 'Nikon-D700')),
    (r'D1x', ('camera', 'Nikon-D1x')),
    (r'D1s', ('camera', 'Nikon-D1s')),
    (r'D2x', ('camera', 'Nikon-D2x')),
    (r'D2H', ('camera', 'Nikon-D2H')),
    (r'Nikon.*D2x', ('camera', 'Nikon-D2x')),
    (r'Nikon.*D-?60', ('camera', 'Nikon-D60')),
    (r'Nikon.*D-?50', ('camera', 'Nikon-D50')),
    (r'Nikon.*D-?40x', ('camera', 'Nikon-D40x')),
    (r'Nikon 40X', ('camera', 'Nikon-D40x')), #JuhaniLaiho
    (r'Nikon.*D-?40', ('camera', 'Nikon-D40')),
    (r'D70s', ('camera', 'Nikon-D70s')),
    (r'D70', ('camera', 'Nikon-D70')),
    (r'D200', ('camera', 'Nikon-D200')),
    (r'D90', ('camera', 'Nikon-D90')),
    (r'Nikon FM2', ('camera', 'Nikon-FM2')),
    (r'Nikon FM3', ('camera', 'Nikon-FM3')), # Must be above CP5k because of scanners
    (r'Nikon FE2', ('camera', 'Nikon-FE2')),
    (r'Nikon F80', ('camera', 'Nikon-F80')),
    (r'(Nikon|Coolpix).*950', ('camera', 'Nikon-CP950')),
    (r'(Nikon|Coolpix).*990', ('camera', 'Nikon-CP990')),
    (r'(Nikon|Coolpix).*995', ('camera', 'Nikon-CP995')),
    (r'(Nikon|Coolpix).*2100', ('camera', 'Nikon-CP2100')),
    (r'(Nikon|Coolpix).*4300', ('camera', 'Nikon-CP4300')),
    (r'(Nikon|Coolpix).*4500', ('camera', 'Nikon-CP4500')),
    (r'(Nikon|Coolpix).*5000', ('camera', 'Nikon-CP5000')),
    (r'(Nikon|Coolpix).*P *5100', ('camera', 'Nikon-P5100')), # Performance model
    (r'(Nikon|Coolpix).*5100', ('camera', 'Nikon-CP5100')),
    (r'(Nikon|Coolpix).*5200', ('camera', 'Nikon-CP5200')),
    (r'(Nikon|Coolpix).*5400', ('camera', 'Nikon-CP5400')), #E5400
    (r'(Nikon|Coolpix|CP).*5700', ('camera', 'Nikon-CP5700')),
    (r'(Nikon|Coolpix).*8400', ('camera', 'Nikon-CP8400')),
    (r'(Nikon|Coolpix).*8700', ('camera', 'Nikon-CP8700')),
    (r'(Nikon|Coolpix).*8800', ('camera', 'Nikon-CP8800')),
    
    # This one old canon film camera...
    (r'D10', ('camera', 'Canon-D10')),

    # Fuji
    (r'(Fuji|Fine ?pix).*S5.*Pro', ('camera', 'Fuji-S5Pro')),
    (r'(Fuji|Fine ?pix).*S5', ('camera', 'Fuji-S5')),
    (r'(Fuji|Fine ?pix).*S4.*Pro', ('camera', 'Fuji-S4Pro')),
    (r'(Fuji|Fine ?pix).*S4', ('camera', 'Fuji-S4')),
    (r'(Fuji|Fine ?pix).*S3.*Pro', ('camera', 'Fuji-S3Pro')),
    (r'(Fuji|Fine ?pix).*S3', ('camera', 'Fuji-S3')),
    (r'(Fuji|Fine ?pix).*S2.*Pro', ('camera', 'Fuji-S2Pro')),
    (r'(Fuji|Fine ?pix).*S2', ('camera', 'Fuji-S2')),
    (r'Fine ?Pix.*A345', ('camera', 'Fuji-A345'), ('lens', 'builtin')),
    (r'Fine ?Pix.*A500', ('camera', 'Fuji-A500'), ('lens', 'builtin')),
    (r'Fuji.*S7000', ('camera', 'Fuji-S7000')),
    (r'Fuji.*S9600', ('camera', 'Fuji-S9600')),

    # Olympus
    (r'Oly[mn]pus E-?3\b', ('camera', 'Olympus-E3')),
    (r'Oly[mn]pus E-?30\b', ('camera', 'Olympus-E30')),
    (r'Oly[mn]pus E-?410\b', ('camera', 'Olympus-E410')),
    (r'E[ -]?300', ('camera', 'Olympus-E300')),
    (r'E[ -]?500', ('camera', 'Olympus-E500')),
    (r'Olympus 5050', ('camera', 'Olympus-5050')),
    (r'Olympus C-7070WZ', ('camera', 'Olympus-C7070WZ')),
    (r'Olympus C-7070', ('camera', 'Olympus-C7070')), #FIXME are these the same?
    (r'Olympus FE-310', ('camera', 'Olympus-FE310')),

    # Pentax
    (r'Pentax.*ist ?DS', ('camera', 'Pentax-istDS')),
    (r'Pentax.*ist ?DL', ('camera', 'Pentax-istDL')),
    (r'Pentax.*ist ?D', ('camera', 'Pentax-istD')),
    (r'Pentax.*K10D', ('camera', 'Pentax-K10D')),
    (r'Pentax.*K20D', ('camera', 'Pentax-K20D')),
    (r'Samsung GX10', ('camera', 'Samsung-GX10')), #DPReview says same as K10D
    (r'Pentax.*K100D', ('camera', 'Pentax-K100D')),
    (r'Pentax K200', ('camera', 'Pentax-K200')),
    (r'Optio W10', ('camera', 'Pentax-OptioW10')),
    (r'Pentax MZ-5', ('camera', 'Pentax-MZ5')),

    # Sony
    (r'Sony (Alpha|DSLR-A) *700', ('camera', 'Sony-DSLRA700')),
    (r'Sony A230', ('camera', 'Sony-A230')),
    
    # Others
    (r'Sigma SD9', ('camera', 'Sigma-SD9')),
    (r'Sigma SD10', ('camera', 'Sigma-SD10')),
    (r'Ricoh Caplio GX|Rollei 5100', ('camera', 'Ricoh-CapiloGX')),
    (r'Bessa-L', ('camera', 'Voigtlaender-BessaL')),
    (r'Minolta (Dynax )?7D', ('camera', 'Minolta-Dynax7D')),
    (r'Yashica FX107', ('camera', 'Yashica-FX107')),
    (r'Leica M6TTL', ('camera', 'Leica M6TTL')),
    (r'Leica Digilux 3', ('camera', 'Leica-Digilux3')),

    # Can't take addons
    (r'Brownie', ('camera', 'Kodak-Brownie')),
    (r'Olympus C-3020', ('camera', 'Olympus-C3020')),
    (r'Olympus D-40', ('camera', 'Olympus-D40')),
    (r'Canon G1', ('camera', 'Canon-G1')),
    (r'Canon G3', ('camera', 'Canon-G3')),
    (r'Canon G5', ('camera', 'Canon-G5')),
    (r'DX3900', ('camera', 'Kodak-DX3900'), ('lens', 'builtin')),
    (r'Olympus E-1', ('camera', 'Olympus-E1')),
    (r'Minolta.*A200', ('camera', 'Minolta-A200')),
    (r'Minolta A2', ('camera', 'Minolta-A2')), #Same as prev?
    (r'Dimage 7Hi', ('camera', 'Minolta-Dimage7Hi')),
    (r'Dimage 7', ('camera', 'Minolta-Dimage7')),
    (r'Dimage', ('camera', 'Minolta-DimageZ1')),
    (r'PowerShot.*A75', ('camera', 'Canon-PowerShotA75'), ('lens', 'builtin')),
    (r'Power *Shot.*A *610', ('camera', 'Canon-PowerShotA610'), ('lens', 'builtin')),
    (r'Canon A40', ('camera', 'Canon-PowerShotA40'), ('lens', 'builtin')),
    (r'Canon.*A60', ('camera', 'Canon-PowerShotA60'), ('lens', 'builtin')),
    (r'Canon A80', ('camera', 'Canon-PowerShotA80'), ('lens', 'builtin')),
    (r'PowerShot.*A510', ('camera', 'Canon-PowerShotA510'), ('lens', 'builtin')),
    (r'PowerShot.*A520', ('camera', 'Canon-PowerShotA520'), ('lens', 'builtin')),
    (r'PowerShot.*S60', ('camera', 'Canon-PowerShotS60'), ('lens', 'builtin')),
    (r'PowerShot.*S230', ('camera', 'Canon-PowerShotS230'), ('lens', 'builtin')),
    (r'Power *Shot.*A *710', ('camera', 'Canon-PowerShotA710'), ('lens', 'builtin')),
    (r'Olympus FE-?210', ('camera', 'Olympus-FE210'), ('lens', 'builtin')),
    (r'(Sony|Cybershot)( DSC)? F717', ('camera', 'Sony-CybershotF717')),
    (r'(Sony|Cybershot)( DSC)? ?s?85', ('camera', 'Sony-CybershotDSC85')), #Booboo, S85?
    (r'Cybershot( DSC)? F707', ('camera', 'Sony-CybershotDSCF707')),
    (r'Sony CyberShot W5', ('camera', 'Sony-CybershotW5')),
    (r'Sony DSC-P100', ('camera', 'Sony-CybershotDSCP100')),
    (r'Sony DSC-R1', ('camera', 'Sony-CybershotDSCR1')),
    (r'Sony MVC-CD500', ('camera', 'Sony-MVCCD500')),
    (r'Sony Ixus 60', ('camera', 'Sony-IXUS60')),
    (r'roundshot', ('camera', 'Seitz-Roundshot')),
    (r'Kodak DC290', ('camera', 'Kodak-DC290')),
    (r'Kodak DC380', ('camera', 'Kodak-DC290')),
    (r'Kodak[ -]?DCS Pro', ('camera', 'Kodak-DCSPro')),
    (r'Panasonic LC5', ('camera', 'Panasonic-LC5')),
    (r'Pentax Optio 60', ('camera', 'Pentax-Optio60')),
    (r'Sa[mn]sung.*s730', ('camera', 'Samsung-S730')),
    (r'Panasonic FZ50', ('camera', 'Panasonic-FZ50')),
    (r'Panasonic DMC-LX2', ('camera', 'Panasonic-DMCLX2')),
    (r'samsung GX 10', ('camera', 'Samsung-GX10')),
    (r'Canon Optura 30', ('camera', 'Canon-Optura30')),
    (r'Olympus SP550', ('camera', 'Olympus-SP550')),
    # Scanning cams
    (r'Panoscan\s*MK3', ('camera', 'Panoscan-MK3'), ('panohead', 'Panoscan-MK3')),

    # Medium format
    (r'Mamiya 7II', ('camera', 'Mamiya-7II')),
    (r'6x7', ('camera', 'Medium-?')),

    # Generic
    (r'Canon', ('camera', 'Canon-?')),
    (r'Nikon', ('camera', 'Nikon-?')),
    (r'Kodak', ('camera', 'Kodak-?')),
    (r'Pentax', ('camera', 'Pentax-?')),
    (r'Fuji', ('camera', 'Fuji-?')),
    (r'Sony', ('camera', 'Sony-?')),
    (r'Panasonic', ('camera', 'Panasonic-?')),
    ],

    [
    # Lenses
    (r'Epoque Wide Convert.*0\.56x', ('lens', 'Epoque-WE0.56')), #Must be before 10.5

    (r'8mm Zuiko|Zuiko\s+(?:lens\s+)?8\s*mm|Olympus 8mm|ED 8mm 3\.5', ('lens', 'Zuiko-8mm')), #Bain
    (r'14-104mm', ('lens', '??-14to104mm')), #Bain
    (r'Zuiko 13-45', ('lens', 'Zuiko-14to45mm')), #HenkKeijzer
    (r'Peleng?|pelleng', ('lens', 'Peleng-8mm')),
    (r'Sigma 4\.5', ('lens', 'Sigma-4.5mm2.8')),
    (r'Sigma f3.5 8mm|Sigma 8mm f3.5|Sigma 8mm/F3,5', ('lens', 'Sigma-8mm3.5')), #FIXME: verify there are not others
    (r'Sigma 8mm/f4|Sigma fisheye 8mm f:4', ('lens', 'Sigma-8mmf4')),
    (r'Sigma.*\b8 ?mm|sigma[ -]?8| S 8mm|8mm sigma|sigma 4/8', ('lens', 'Sigma-8mm')),
    (r'15mm.*Sigma|Sigma.*15mm|sigma *15', ('lens', 'Sigma-15mm')),
    (r'Sigma 14/|sigma 14mm|14mm lenss', ('lens', 'Sigma-14mm')),
    (r'Can+on.*15 ?mm|1DS.*15mm (?:f2\.8)?', ('lens', 'Canon-15mm')),
    (r'Canon.*28-200mm', ('lens', 'Canon-28to200mm')),
    (r'[Ss]haved.*10[.,]5|10[.,]5.*[Ss]haved', ('lens', 'Nikkor-10.5mm-Shaved')),
    (r'(Nikkor|Nikon)\s*10\.5|Nikon 10mm', ('lens', 'Nikkor-10.5mm')),
    (r'10\.5|10,5', ('lens', 'Nikkor-10.5mm')), # Unsure...
    (r'Tokina.*[Ss]haved.*10-17|Tokina.*10-17.*[Ss]haved|'
     r'[Ss]haved.*Tokina.*10-17|Tokina AT-X 107 \(shaved\)', ('lens', 'Tokina-10to17mm-Shaved')),
    (r'Tokina.*10-17( *mm)?', ('lens', 'Tokina-10to17mm')),
    (r'Tokina *107', ('lens', 'Tokina-10to17mm')),
    (r'Tokina.*12', ('lens', 'Tokina-12to24mm')),
    (r'Tamron.*11', ('lens', 'Tamron-11to18mm')),
    (r'Tamron 17-50', ('lens', 'Tamron-17to50mm')),
    (r'Tokina 17mm|17 mm Tokina', ('lens', 'Tokina-17mm')),
    (r'Zenitar.*16(mm)?', ('lens', 'Zenitar-16mm')),
    (r'FC[ -]?E?8|EC[ -]?8|Nikon E8', ('lens', 'Nikon-FCE8')),
    (r'FC[ -]?[0E]?9', ('lens', 'Nikon-FCE9')), #JamesGentles says FC-09
    (r'E24', ('lens', 'Nikon-WCE24')),
    (r'E63', ('lens', 'Nikon-WCE63')),
    (r'Nikkor.*17-35', ('lens', 'Nikkor-17to35mm')),
    (r'16mm Nikkor', ('lens', 'Nikkor-16mm')),
    (r'(Nikkor|Nikon).*17-55', ('lens', 'Nikkor-17to55mm')),
    (r'Nikon.*18mm-70mm', ('lens', 'Nikkor-18to70')), #FIXME: verify no others
    (r'Sigma.*18-55', ('lens', 'Sigma-18to55mm')),
    (r'Sigma.*18mm', ('lens', 'Sigma-18mm')), #f3.5
    (r'Sigma.*18-125', ('lens', 'Sigma-18to125mm')),
    (r'Sigma.*10-20', ('lens', 'Sigma-10to20mm')), #SarahDuplisea, is this the Canon?
    (r'Sigma.*12-24', ('lens', 'Sigma-12to24mm')),
    (r'Sigma.*17-35', ('lens', 'Sigma-17to35mm')), #F2.8-4
    (r'15 - 30 mm Sigma', ('lens', 'Sigma-15to30mm')),
    (r'(Nikon|Nikkor).*18-70', ('lens', 'Nikkor-18to70mm')),
    (r'DA.*10-17|Pentax 10-17', ('lens', 'Pentax-DA10to17mm')),
    (r'dcr.*185', ('lens', 'Raynox-DCR185')),
    (r'fe180(pro)?', ('lens', 'Raynox-FE180')), #ScottDoenges
    (r'Raynox (fisheye|wide)', ('lens', 'Raynox-?')),
    (r'Raynox .65', ('lens', 'Raynox-0.65')),
    (r'10-22 *(?:mm|ef-?s)', ('lens', 'Canon-10to22mm')),
    (r'Canon.*16-35', ('lens', 'Canon-16to35mmL')),
    (r'Canon.*17-40', ('lens', 'Canon-17to40mmL')),
    (r'Canon.*17-85', ('lens', 'Canon17to85mm')), #Canon EF-S 17-85mm F4-5.6 IS USM
    (r'Canon.*24-104', ('lens', 'Canon24to104mmL')), #F4L
    (r'Samsung.*kit lens 18-55', ('lens', 'Samsung-18to55')),
    (r'18-55|Canon Rebel.*18mm|400D.*Kit Lens', ('lens', 'Canon-18to55mm')),
    #990.*wide.angl -> wce24?
    (r'Nikon.*[45].00.*E8', ('lens', 'Nikon-FCE8')),
    (r'Nikon.*[45].00.*fisheye', ('lens', 'Nikon-FCE9')),
    (r'Nikon.*[45].00.*wide angle', ('lens', 'Nikon-WCE24')), #Ask Gabi.
    (r'Minolta.*7.2-50.8 mm', ('lens', 'Minolta-7.2to50.8mm')),
    (r'Minolta Dimage.*(28mm|wide angle)', ('lens', 'Minolta-WE')), #FIXME
    (r'Olympus.*14-54|14mm Olympus', ('lens', 'Olympus-14to54mm')),
    (r'Nikon 12-24', ('lens', 'Nikkor-12to24mm')),
    (r'Nik+or 8(?:mm)?|8mm nikkor|Nikon 8mm', ('lens', 'Nikkor-8mm')), # 8mm.{,10}2.8
    (r'20.*Nikkor', ('lens', 'Nikkor-20mm')), #This is too broad.
    (r'12 mm \(?rectilinear\)? ultra', ('lens', '?-12mm')), # Same guy as the next one.
    (r'12 mm Heliar|Ultra-Heliar 12', ('lens', 'Heliar-12mm')),
    (r'15 mm Heliar', ('lens', 'Heliar-15mm')),
    (r'PC-Super-Angulon.*28mm', ('lens', 'Schneider-28mm')),
    (r'Soligor fisheye.*0,25x', ('lens', 'Soligor-WE')),
    (r'Soligor Fisheye', ('lens', 'Soligor-WE')), # Seems there is only one?
    (r'Leica 16mm Fisheye', ('lens', 'Leica-16mm')),
    (r'Pentax.*10-17mm', ('lens', 'Pentax-10to17mm')),
    (r'Pentax 14mm', ('lens', 'Pentax-14mm')),
    (r'Coa?stal Optic(al|s|)', ('lens', 'CoastalOptical-4.88mm')), #185deg!
    (r'WCON-07C', ('lens', 'Olympus-WCON07C')),
    
    (r'Nikkor 55-200', ('lens', 'Nikkor-55to200mm')),
    (r'Canon.*50mm', ('lens', 'Canon-50mm')), #CarolingGeary
    (r'Nikon.*40mm', ('lens', 'Nikkor-40mm??')), #CraigABusch
    (r'\b8 *mm', ('lens', '??-8mm')), #AndrzejHarasz
    (r'Sigma', ('lens', 'Sigma-?')),
    (r'10-22|Canon.*10mm', ('lens', 'Canon-10to22mm')), #CBArunKumar, MarkCrawford
    (r'canon[\w\W]+15mm', ('lens', 'Canon-15mm')), #JonathanGreet
    ],

    [
    # Tripods
    (r'monopod Manfrotto|Manfrotto monopod', ('tripod', 'Manfrotto-Monopod'), ('panohead', 'none')),
    (r'monopod|nodalpod', ('tripod', 'Monopod'), ('panohead', 'none')),
    (r'bi[ -]?pod', ('tripod', 'Bipod')),
    (r'no tripod', ('tripod', 'none')),
    (r'Manfrotto 190', ('tripod', 'Manfrotto-190')),
    (r'Manfrotto 682B', ('tripod', 'Manfrotto-682B')),
    (r'3001D', ('tripod', 'Manfrotto-3001d')),
    (r'(Bogen|Manfrotto) 3000', ('tripod', 'Manfrotto-3000')),
    (r'(Bogen|Manfrotto) 3021', ('tripod', 'Manfrotto-3021')), #Methinks this is the same as the next.
    (r'3021B', ('tripod', 'Manfrotto-3021b')),
    (r'(Bogen|Manfrotto) 3201', ('tripod', 'Manfrotto-3201')),
    (r'742B', ('tripod', 'Manfrotto-742b')),
    (r'Manfrot+o 0?58', ('tripod', 'Manfrotto-058')),
    (r'Manfrot+o 0?55|055(pro)? manfrotto', ('tripod', 'Manfrotto-055')), #-CB
    (r'055 tripod', ('tripod', 'Manfrotto-055')),
    (r'Manfrotto 505', ('tripod', 'Manfrotto-505')), #-PROB
    (r'Manfrotto 755B', ('tripod', 'Manfrotto-755B')), # Same as next?
    (r'Manfrotto 755MF3', ('tripod', 'Manfrotto-755MF3')),
    (r'Manfrotto 679b', ('tripod', 'Manfrotto-679b')),
    (r'Manfrotto Neotec', ('tripod', 'Manfrotto-Neotec')), #VivekDevBurman
    (r'Manfroto Light Stand', ('tripod', 'Manfrotto-LightStand')),
    (r'vanguard', ('tripod', 'Vanguard-?')),
    (r'Velbon Carmagne', ('tripod', 'Velbon-Carmagne')),
    (r'Velbon Sherpa', ('tripod', 'Velbon-Sherpa')),
    (r'Velbon Ultra Lux i SF', ('tripod', 'Velbon-UltraLuxISF')),
    (r'Velbon VGB-3', ('tripod', 'Velbon-VGB3')),
    (r'velbr?on', ('tripod', 'Velbon-?')),
    (r'Gizo 1027', ('tripod', 'Gitzo-1027')),
    (r'gitzo G?1325', ('tripod', 'Gitzo-G1325')),
    (r'Gitzo G?1329', ('tripod', 'Gitzo-G1329')),
    (r'Gitzo G?2220', ('tripod', 'Gitzo-G2220')),
    (r'Gitzo G?2227', ('tripod', 'Gitzo-G2227')),
    (r'Gitzo G?1227', ('tripod', 'Gitzo-G1227')),
    (r'Gitzo G? *1228', ('tripod', 'Gitzo-G1228')),
    (r'Benro 227 CF', ('tripod', 'Benro-227CF')),
    (r'Benro C-427', ('tripod', 'Benro-C427')),
    (r'Feisol Traveller CT3441', ('tripod', 'Feisol-TravellerCT3441')),
    (r'gitzo', ('tripod', 'Gitzo-?')),
    (r'feisol', ('tripod', 'Feisol-?')),
    (r'benbo', ('tripod', 'Benbo-?')),
    (r'benro', ('tripod', 'Benro-?')),
    (r'Vivitar 2200', ('tripod', 'Vivitar-2200')),
    (r'Hakuba 504-MX', ('tripod', 'Hakuba-504MX')),
    (r'MDeVe aluminum video', ('tripod', 'MDeVe-aluminumvideo')),
    (r'Sleek Pro 500DX', ('tripod', 'Slik-Pro500DX')), #RodrigoAlarconCielock
    (r'Slik Sprint Pro', ('tripod', 'Slik-SprintPro')),
    (r'SLIK ProII', ('tripod', 'Slik-ProII')),
    (r'Slik Able 300 DX', ('tripod', 'Slik-Able300DX')),
    (r'Induo Tripod', ('tripod', 'Induo-?')),
    (r'slik', ('tripod', 'Slik-?')),
    (r'DynaTran', ('tripod', 'DynaTran-?')),
    (r'Hama Tripod', ('tripod', 'Hama-?')),
    (r'(?<!pro )(manfrot+o|bogen|monfrotto|manforo)(?!\s+head|\s+qtvr|\s+rotat|\s+pano|\s+(?:SP)?303)', ('tripod', 'Manfrotto-?')),
    (r'Calumet', ('tripod', 'Calumet-?')),
    (r'manfredo', ('tripod', 'Manfredo-?')),
    (r'tripod|head', ('tripod', 'yes')),
    ],

    [
    # Panoheads
    (r'helicopter|Jet Ranger', ('panohead', 'Helicopter')),
    (r'kite', ('panohead', 'Kite')), #FIXME: is this a tripod?
    
    (r'bophoto|\bbo\b.*bracket', ('panohead', 'LensRing-BoPhoto')),
    (r'agnos lense?\s*(bracket|ring)', ('panohead', 'LensRing-Agnos')),
    (r'lens ring|ring mount', ('panohead', 'LensRing-?')),
    (r'Rotopan', ('panohead', 'Rotospan')),
    (r'jasper (engineering )?panohead', ('panohead', 'Jasper')), #AndyAplern
    (r'RingTS8', ('panohead', 'RingTS8')), #FIXME: what brand?
    
    (r'300N', ('panohead', 'Manfrotto-300n')),
    (r'304.*SPH|SPH.*304', ('panohead', 'Manfrotto-304sph')),
    (r'303.*SPH|SPH?.*303|Manfrotto (art )?303(plus)?', ('panohead', 'Manfrotto-303sph')), # is the SP303PLUS separate?
    (r'302.*SPH|SPH.*302|manfratoo 302', ('panohead', 'Manfrotto-302sph')),
    (r'(Manfrotto|Manfrtoto) QTVR', ('panohead', 'Manfrotto-QTVR')), #302+
    (r'Manfrotto SPH330|Bogen SPH 330', ('panohead', 'Manfrotto-303sph')), #Only Uri uses this!!
    
    (r'kiwi|kaidan.*990', ('panohead', 'Kaidan-Kiwi')), #is the Kiwi-L separate?
    (r'(quickpan|qp)[ -]?iv', ('panohead', 'Kaidan-QuickPanIV')),
    (r'(quickpan|qp)[ -]?(iii|3)', ('panohead', 'Kaidan-QuickPanIII')),
    (r'(quickpan|qp)[ -]?s[1p]', ('panohead', 'Kaidan-QuickPanSpherical')),
    (r'quickpan', ('panohead', 'Kaidan-QuickPan?')),
    (r'Kaidan 360 one', ('panohead', 'Kaidan-360one')),
    (r'kaidan|kiadan|kadian', ('panohead', 'Kaidan-?')),
    
    (r'Panosau?rus|Panasauras|Panasorus', ('panohead', 'Panosaurus')),
    (r'KingPano|pano ?king', ('panohead', 'KingPano')),
    (r'pinnacle vr', ('panohead', 'PinnacleVR')),
    (r'Really Right Stuff', ('panohead', 'ReallyRightStuff')),
    (r'Acratech', ('panohead', 'Acratech')),

    (r'Agno.*s cubic', ('panohead', 'Agnos-cubic')),
    (r'Agno.*s TCPRotator', ('panohead', 'Agnos-TCPRotator')),
    (r'Agno.*s TCPShort', ('panohead', 'Agnos-TCPShort')),
    (r'MrotatorB', ('panohead', 'Agnos-MRotatorB')),
    (r'MrotatorC', ('panohead', 'Agnos-MRotatorC')),
    (r'Mrotator *TCPshort', ('panohead', 'Agnos-MrotatorTCPShort')),
    (r'Mrotator *TCP', ('panohead', 'Agnos-MRotatorTCP')),
    (r'Mrotator *TCS', ('panohead', 'Agnos-MRotatorTCS')),
    (r'Mrotator *UT', ('panohead', 'Agnos-MRotatorUT')),
    (r'Mrotator *U', ('panohead', 'Agnos-MRotatorU')),
    (r'Mrotator', ('panohead', 'Agnos-MRotator?')),
    (r'QuicklyQT ?cubic', ('panohead', 'Agnos-QuicklyQTCubic')),

    #FIXME: 360 Precision Absolute separate?
    (r'360[ -]?precision|P360|360P', ('panohead', '360precision')),
    (r'3sixty', ('panohead', 'Peaceriver-3Sixty')),
    (r'Wasserrohrschelle', ('panohead', 'Wasserrohrschelle')), #Must be before Novoflex

    (r'Novoflex', ('panohead', 'Novoflex')),
    (r'Arca Swiss Monoball', ('panohead', 'ArcaSwiss-Monoball')),
    (r'roundshot *(vr|panohead)', ('panohead', 'Seitz-RoundshotVR')),
    (r'Seitz VRdrive', ('panohead', 'Seitz-VRdrive')),
    (r'Nodal Ninja 5 BETA', ('panohead', 'NodalNinja-5Beta')),
    (r'NN5|Nodal Ninja 5', ('panohead', 'NodalNinja-5')),
    (r'NN4|Nodal Ninja 4', ('panohead', 'NodalNinja-4')),
    (r'NN3|Nod[ae]l[ -]?Ninja ?3', ('panohead', 'NodalNinja-3')),
    (r'NN2|Nodal Ninja 2', ('panohead', 'NodalNinja-2')),
    (r'Ninja SPH-1', ('panohead', 'NodalNinja-SPH1')),
    (r'Ninja SPH-2', ('panohead', 'NodalNinja-SPH2')),
    (r'Nodal[ -]?Ninja', ('panohead', 'NodalNinja-?')),
    
    (r'philopod', ('panohead', 'none'), ('tripod', 'Monopod-Philopod')),
    (r'hand[ -]?(held|hold)|free[ -]?hand', ('panohead', 'none'), ('tripod', 'handheld')), #FIXME
    (r'without( any)? pano-?head', ('panohead', 'none')),
    
    #FIXME: some people are picky.
    #FIXME: this should imply tripod=yes
    (r'own construction', ('panohead', 'custom')),
    (r'(custom|self|home|simple|own|makeshift|inhouse)[^.,]+(head|bracket|mount|adapter)', ('panohead', 'custom')),
    (r'Head: self made|Hand made panorama mount', ('panohead', 'custom')),
    
    # Last ditch...
    (r'Manfrotto.*302', ('panohead', 'Manfrotto-302')), #TudorJenkins
    (r'Manfrotto[ a-z]+head', ('panohead', 'Manfrotto-?')), #NickCrossland
    (r'unbranded pano-head', ('panohead', 'yes')),
    (r'precision', ('panohead', '360precision')),
    (r'seitz', ('panohead', 'Seitz-?')),
    (r'ipix rotator', ('panohead', 'IPIX-?')),
    ],
    
    [
    # Software
    (r'ipix', ('software', 'IPIX')),
    (r'pt.*gui[^.,]*4\.1', ('software', 'Ptgui-4.1')),
    (r'pt.*gui[^.,]*5\.0', ('software', 'Ptgui-5.0')),
    (r'pt.*gui[^.,]*5\.8', ('software', 'Ptgui-5.8')),
    (r'pt.*gui[^.,]6\.3', ('software', 'Ptgui-6.3')),
    (r'pt.*gui[^.,]*6\b', ('software', 'Ptgui-6')),
    (r'pt.*gui[^.,]*(pro\s*(v\.)?7\.2|7\.2\s*pro)', ('software', 'PtguiPro-7.2')),
    (r'pt.*gui[^.,]*(pro\s*(v\.)?7\.3|7\.3\s*pro)', ('software', 'PtguiPro-7.3')),
    (r'pt.*gui[^.,]*(pro\s*(v\.)?7\.4|7\.4\s*pro)', ('software', 'PtguiPro-7.4')),
    (r'pt.*gui[^.,]*(pro\s*(v\.)?7\.5|7\.5\s*pro)', ('software', 'PtguiPro-7.5')),
    (r'pt.*gui[^.,]*(pro\s*(v\.)?7\.6|7\.6\s*pro)', ('software', 'PtguiPro-7.6')),
    (r'pt.*gui[^.,]*(pro\s*(v\.)?7\.7|7\.7\s*pro|pro ver 7\.7)', ('software', 'PtguiPro-7.7')),
    (r'pt.*gui[^.,]*(pro\s*(v\.)?7\.8|7\.8\s*pro)', ('software', 'PtguiPro-7.8')),
    (r'pt.*gui[^.,]*(pro\s*(v\.|ver\s*)?8\.2\.1|8\.2\.1\s*pro)', ('software', 'PtguiPro-8.2.1')),
    (r'pt.*gui[^.,]*(pro\s*(v\.|ver\s*)?8\.2|8\.2\s*pro)', ('software', 'PtguiPro-8.2')),
    (r'pt.*gui[^.,]*(pro\s*(v\.|ver\s*)?8\.0\.?2|8\.02\s*pro)', ('software', 'PtguiPro-8.02')),
    (r'ptgui pro 8 ', ('software', 'PtguiPro-8')), # Don
    (r'pt.*gui[^.,]*7\.2', ('software', 'Ptgui-7.2')),
    (r'pt.*gui[^.,]*7\.3', ('software', 'Ptgui-7.3')),
    (r'pt.*gui[^.,]*7\.4', ('software', 'Ptgui-7.4')),
    (r'pt.*gui[^.,]*7\.5', ('software', 'Ptgui-7.5')),
    (r'pt.*gui[^.,]*7\.6', ('software', 'Ptgui-7.6')),
    (r'pt.*gui[^.,]*7\.7', ('software', 'Ptgui-7.7')),
    (r'pt.*gui[^.,]*8\.02', ('software', 'Ptgui-8.02')),
    (r'pt.*gui[^.,]*8\.1\.5', ('software', 'Ptgui-8.1.5')),
    (r'pt.*gui[^.,]*8\.2\.1', ('software', 'Ptgui-8.2.1')),
    (r'ptgui 7 beta7', ('software', 'Ptgui-7.7')), # I'm not this picky currently.
    (r'ptguimac', ('software', 'PtGui-?')),
    (r'pt.*gui[^.,]*pro', ('software', 'PtguiPro-?')),
    (r'pt.*gui', ('software', 'Ptgui-?')),
    (r'pt.*mac[^.,]*4\.1', ('software', 'PTmac-4.1')),
    (r'pt.*mac[^.,]*3', ('software', 'PTmac-3')),
    (r'pt.*mac', ('software', 'PTmac-?')),
    (r'quicktime.*vr.*studio|qtvr[ -]?as|quicktime\s+virtual\s+reality\s+studio', ('software', 'QTVRAS')),
    (r'stitcher V?4\b', ('software', 'RealvizStitcher-4')),
    (r'stitcher.*5[.,]6', ('software', 'RealvizStitcher-5.6')),
    (r'stitcher.*5[.,]5', ('software', 'RealvizStitcher-5.5')),
    (r'stitcher.*5[.,]1', ('software', 'RealvizStitcher-5.1')),
    (r'[Ss]titcher.*5(?:\.0)?', ('software', 'RealvizStitcher-5.0')),
    (r'stitcher.*3\.1', ('software', 'RealvizStitcher-3.1')),
    (r'realviz.*stitcher|stitcher.*(?:unlimited|UL)', ('software', 'RealvizStitcher-?')),
    (r'stitcher express', ('software', 'Realviz-Stitcher-Express')),
    (r'calico[ -]?1\.2', ('software', 'Calico-1.2')),
    (r'calico', ('software', 'Calico-?')),
    (r'vr[ -]?wor(ks|x)', ('software', 'VRWorx')),
    (r'easy[ -]?pano', ('software', 'EasyPano')), #Should this be above PTGui?
    (r'panoweaver|pw3', ('software', 'Panoweaver')), #This is by EasyPano!
    (r'hugin', ('software', 'Hugin')),
    (r'pano(rama)?[ -]?tools?', ('software', 'PanoTools')),
    (r'panorama factory', ('software', 'PanoramaFactory')),
    (r'Canon photostitch', ('software', 'CanonPhotoStitch')),
    (r'Autopano', ('software', 'Autopano')),
    (r'autostitch', ('software', 'Autostitch')),
    (r'panolab', ('software', 'PanoLab')), #' 0.8'
    (r'pano(rama)?[ -]?studio 1\.4\.1', ('software', 'PanoramaStudio-1.4.1')),
    
    (r'realviz|stitcher', ('software', 'RealvizStitcher-?')),

    (r'photo ?shop|cs2|ps-cs', ('software', 'Photoshop')), # Remove this if it's added to something else
    (r'PSP|Paint[ -]?Shop', ('software', 'PaintShopPro')),
    (r'Photo Paint', ('software', 'PhotoPaint')),
    ],

    [
    #QTVR maker
    (r'Pano2QTVR(pro)?', ('qtvr', 'Pano2QTVR')),
    (r'cubic ?converter', ('qtvr', 'CubicConverter')),
    (r'make ?cubic', ('qtvr', 'MakeCubic')),
    (r'pano ?cube', ('qtvr', 'PanoCube')),
    (r'quickly ?pano', ('qtvr', 'QuicklyPano')),
    (r'Equi2QTVR', ('qtvr', 'Equi2QTVR')),
    ],

    [
    #Blender
    (r'X[ -]?blend', ('blender', 'XBlend')),
    (r'Smart[ -]?blend', ('blender', 'SmartBlend')),
    (r'E[mn][ -]?Blend', ('blender', 'EnBlend')),
    ],

    #leveler/rotator: Bogen rotator
    #films: Fuji NPZ 800, (Fuji )?Reala, Fuji Provia, slide film
    #HDR: Photomatix, Leung.*(HDR|action), HDR for Dummies
    #Pole: pole
]

hier = {
    ('camera', 'Nikon-D50'): [('Nikon', 'DSLR', 'D50')],
    ('camera', 'Nikon-D70'): [('Nikon', 'DSLR', 'D70')],
    ('camera', 'Nikon-D70s'): [('Nikon', 'DSLR', 'D70s')],
    ('camera', 'Nikon-D80'): [('Nikon', 'DSLR', 'D80')],
    ('camera', 'Nikon-D100'): [('Nikon', 'DSLR', 'D100')],
    ('camera', 'Nikon-D200'): [('Nikon', 'DSLR', 'D200')],
    ('camera', 'Canon-5D'): [('Canon', 'DSLR', '5D')],
    ('camera', 'Canon-10D'): [('Canon', 'DSLR', '10D')],
    ('camera', 'Canon-20D'): [('Canon', 'DSLR', '20D')],
    ('camera', 'Canon-300D'): [('Canon', 'DSLR', '300D')],
    ('camera', 'Canon-350D'): [('Canon', 'DSLR', '350D')],
    ('camera', 'Canon-?'): [('Canon', 'Unknown')],
    ('camera', 'Nikon-?'): [('Nikon', 'Unknown')],
}
