# backend/app/discovery/platforms/__init__.py
"""
47 Remote Job Platform Scrapers - Organized by Category

Structure:
- api_scrapers.py: 4 API-based platforms (RemoteOK, Remotive, Working Nomads, Himalayas)
- rss_scrapers.py: 4 RSS-based platforms (WeWorkRemotely, AuthenticJobs, Jobspresso, Nodesk)
- web_scrapers.py: 11 Web scraping platforms (Arc.dev, JustRemote, etc.)
- latam_scrapers.py: 14 LATAM/Brazil platforms (Revelo, GeekHunter, etc.)
- premium_scrapers.py: 14 Premium platforms (Turing, WellFound, etc.)
- master_scraper.py: Orchestrator that runs all scrapers
"""

from .master_scraper import (
    scrape_all_47_platforms,
    scrape_top_platforms_only,
)

from .api_scrapers import (
    scrape_remoteok,
    scrape_remotive,
    scrape_workingnomads,
    scrape_himalayas,
    scrape_all_api_platforms,
)

from .rss_scrapers import (
    scrape_weworkremotely_rss,
    scrape_authenticjobs_rss,
    scrape_jobspresso_rss,
    scrape_nodesk_rss,
    scrape_all_rss_platforms,
)

from .web_scrapers import (
    scrape_arcdev,
    scrape_justremote,
    scrape_jsremotely,
    scrape_hubstaff,
    scrape_landingjobs,
    scrape_pangian,
    scrape_fourdayweek,
    scrape_skipthedrive,
    scrape_totaljobs,
    scrape_gunio,
    scrape_idealist,
    scrape_all_web_platforms,
)

from .latam_scrapers import (
    scrape_revelo,
    scrape_geekhunter,
    scrape_programathor,
    scrape_seujob,
    scrape_coodesh,
    scrape_impulso,
    scrape_tecla,
    scrape_beontech,
    scrape_flatworld,
    scrape_nixa,
    scrape_insquad,
    scrape_distro,
    scrape_loka,
    scrape_kula,
    scrape_all_latam_platforms,
)

from .premium_scrapers import (
    scrape_turing,
    scrape_wellfound_api,
    scrape_vanhack,
    scrape_snaphunt,
    scrape_hired,
    scrape_soshace,
    scrape_strider,
    scrape_powertofly,
    scrape_remote100k,
    scrape_levelsfyi,
    scrape_workatastartup,
    scrape_remotecom,
    scrape_remoteyeah,
    scrape_flexjobs,
    scrape_all_premium_platforms,
)

__all__ = [
    # Main functions
    'scrape_all_47_platforms',
    'scrape_top_platforms_only',
    
    # Category functions
    'scrape_all_api_platforms',
    'scrape_all_rss_platforms', 
    'scrape_all_web_platforms',
    'scrape_all_latam_platforms',
    'scrape_all_premium_platforms',
    
    # Individual scrapers (all 47)
    'scrape_remoteok', 'scrape_remotive', 'scrape_workingnomads', 'scrape_himalayas',
    'scrape_weworkremotely_rss', 'scrape_authenticjobs_rss', 'scrape_jobspresso_rss', 'scrape_nodesk_rss',
    'scrape_arcdev', 'scrape_justremote', 'scrape_jsremotely', 'scrape_hubstaff',
    'scrape_landingjobs', 'scrape_pangian', 'scrape_fourdayweek', 'scrape_skipthedrive',
    'scrape_totaljobs', 'scrape_gunio', 'scrape_idealist',
    'scrape_revelo', 'scrape_geekhunter', 'scrape_programathor', 'scrape_seujob',
    'scrape_coodesh', 'scrape_impulso', 'scrape_tecla', 'scrape_beontech',
    'scrape_flatworld', 'scrape_nixa', 'scrape_insquad', 'scrape_distro', 'scrape_loka', 'scrape_kula',
    'scrape_turing', 'scrape_wellfound_api', 'scrape_vanhack', 'scrape_snaphunt',
    'scrape_hired', 'scrape_soshace', 'scrape_strider', 'scrape_powertofly',
    'scrape_remote100k', 'scrape_levelsfyi', 'scrape_workatastartup',
    'scrape_remotecom', 'scrape_remoteyeah', 'scrape_flexjobs',
]
