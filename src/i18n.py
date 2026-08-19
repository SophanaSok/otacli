TEXTS = {
    "en": {
        "yes": "Yes",
        "no": "No",
        "back": "Back",
        "cancel": "Cancel",
        "currently": "Currently",
        "menu_main": "Main Menu",

        # m_welcome
        "menu_search": "Search",
        "menu_resume": "Continue watching",
        "menu_trending": "Trending Anime",
        "menu_calendar": "Release Calendar",
        "menu_mylist": "My List",
        "menu_library": "My Library (Offline)",
        "menu_history": "Watch History",
        "menu_stats": "otacli Statistics",
        "menu_settings": "Settings",
        "menu_exit": "Exit",
        "welcome_prompt": "Choose what you want to do: ",
        "status_connected": "🟢 STATUS: Connected to AniList!",
        "status_disconnected": "🔴 STATUS: Not connected to AniList (Configure in Settings)",
        
        # m_settings
        "set_anilist": "Connect / Update AniList account",
        "set_dl_path": "Change download path",
        "set_quality": "Change default video quality",
        "set_prompt": "Choose what to configure: ",
        
        
        "al_no_client": "[!] AniList sync is not configured in this build of otacli.",
        "al_no_client_help": "Register an AniList API client at https://anilist.co/settings/developer and set ANILIST_CLIENT_ID in src/main_module.py.",
        "al_info1": "A browser window will open asking you to authorize otacli on your AniList account.",
        "al_info2": "After approving, copy the Token (long string of characters) and paste it below.\n",
        "al_err": "Could not open the browser! Please visit this link manually:\n{}\n",
        "al_input": "Paste your AniList Access Token (or leave empty to cancel):",
        "al_success": "\n[+] Token saved successfully! otacli will now automatically sync your progress.",
        "al_completed": "Completed",
        
        "dl_info": "[INFO] Current download folder: {}",
        "dl_help1": "Enter the full path to the new folder (e.g. D:\\Anime or /home/user/Videos).",
        "dl_help2": "Leave this field empty and press ENTER to restore the default internal folder.\n",
        "dl_input": "Enter new path:",
        "dl_reset": "\n[+] Restored default download folder!",
        "dl_success": "\n[+] Successfully changed save folder to: {}",
        "dl_err": "\n[-] Error creating folder (Invalid path?): {}",
        
        "qual_source": "Source",
        "qual_prompt": "Choose preferred player quality:",
        "qual_success": "\n[+] Quality successfully changed to: {}",
        

        "dl_def_path": "Default",
        
        # m_mylist
        "mylist_sync": "[INFO] Auto-syncing with AniList...",
        "mylist_prompt": "Choose anime: ",
        "mylist_random": "🎲 Random anime from my list",
        
        # m_history
        "hist_prompt": "Select an entry to view details: ",
        "hist_err_server": "Error: Failed to fetch details from the server.",
        "hist_err_profile": "This anime has no assigned profile in Docchi.",
        
        # m_find
        "find_title": "By title",
        "find_title_en": "By title EN",
        "find_mal": "Mal ID",
        "find_genre": "By genre",
        "find_prompt": "Choose how you want to search: ",
        "find_search": "Search: ",
        
        # genres
        "genre_err": "Error: No genres found in the database.",
        "genre_prompt": "Choose a genre you are interested in:",
        "sort_trending": "By popularity (AniList Trending)",
        "sort_alpha": "Alphabetical",
        "sort_surprise": "Surprise me!",
        "sort_prompt": "What do we do next?",
        "genre_res_prompt": "Results for genre [{}] (Found: {}):",
        
        # trending
        "trend_prompt": "Choose: ",
        
        # m_details
        "det_cont": "Continue from episode",
        "det_first": "Watch from episode 1",
        "det_list": "Episode list",
        "det_dl_season": "Download entire season",
        "det_dl_eps": "Download specific episodes",
        "det_rm_list": "Remove from my list",
        "det_add_list": "Add to my list",
        "det_search": "Search engine",
        "det_prompt": "Choose what you want to do: ",
        "det_ep_count": "Episodes count",
        "det_score": "Score",
        "det_dl_input": "Enter episodes to download (e.g. 3 or 4-6 or 1,3,5) [Total eps: {}]:",
        "det_dl_err": "Error: Invalid episode numbers provided!",
        
        # w_list
        "list_err": "Episodes count not found [AniList error or missing MAL ID]",
        "list_prompt": "Choose episode: ",
        
        # w_players
        "pl_load": "[INFO] Episode {} - Loading sources...",
        "pl_pl_src": "Fetching Polish sources (docchi.pl)...",
        "pl_en_src": "Fetching English sources (anidb.app with MAL ID verification)...",
        "pl_404": "Episode not found in any database (PL/EN) [Error 404]",
        "pl_analyzing": "\nAnalyzing, live checking sources, and fetching qualities...",
        "pl_unknown": "Unknown",
        "pl_none": "None",
        "pl_link": "Source link",
        "pl_chg_qual": "Change maximum quality",
        "pl_prompt": "Choose source: ",
        "pl_start": "Starting playback...",
        "pl_err_src": "Selected source is unavailable or not supported!",
        "pl_qual_chg": "Player quality changed to {}",
        
        # w_default
        "def_chg_src": "Change source",
        "def_next": "Next episode",
        "def_rate": "Rate series (AniList)",
        "def_prev": "Previous episode",
        "def_list": "Episode list",
        "def_prompt": "What do you want to do? ",
        "def_qmark": "Episode: {}/{}",
        "def_finish": "Series completed (Return to main menu)",
        "rate_info": "[INFO] Fetching your AniList scoring format...",
        "rate_good": "(Good)",
        "rate_avg": "(Average)",
        "rate_bad": "(Bad)",
        "rate_no": "I don't want to rate",
        "rate_prompt": "How do you rate this series on your scale?",
        "rate_send": "[INFO] Sending rating to AniList...",
        "rate_ok": "[+] Rating successfully saved to your profile!",
        "rate_err": "[-] An error occurred while sending the rating.",
        "finish_msg": "🎉 Congratulations! Anime completed: {}",
        
        # resume
        "res_empty": "No watch history to resume.",
        "res_resume": "Resume: {} (Episode {})",
        "res_prompt": "What do you want to continue?",
        "res_load": "[INFO] Loading data...",
        
        # calendar
        "cal_info": "[INFO] Fetching release calendar from AniList...",
        "cal_err1": "[-] Failed to fetch calendar or no upcoming releases.",
        "cal_days": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "cal_none": "Unknown",
        "cal_err2": "[-] Among the next 50 worldwide releases, none were found in the database.",
        "cal_prompt": "Upcoming releases (Sorted chronologically):",

        # anilist_connector
        "al_no_desc": "No description available.",
        "al_airing_rel": "Airing (Released: {})",
        "al_airing": "Currently airing",
        "al_none": "None",
        "al_sync": "[INFO] Syncing history with AniList (This will take a moment)...",
        "al_skip_no_id": "[-] AniSkip: Missing MAL ID or episode number. Markers disabled.",
        "al_skip_ep": "Episode",
        "al_skip_found": "[+] AniSkip markers found! Generated {} intervals.",
        "al_skip_not_found": "[-] AniSkip database does not have markers for this episode yet.",
        "al_skip_rej": "[-] Rejected by AniSkip server (Error {})",
        "al_skip_err": "[ERROR] AniSkip download failure: {}",

        # cache
        "cache_conn": "[INFO] Connecting to Docchi and AniList servers...",
        "cache_fetch": "[INFO] Fetching database of titles and trending...",


        # docchi_api_connector
        "anidb_dub": "dub",
        "anidb_sub": "sub",
        "anidb_src": "source",

        # downloader
        "dl_err_ep_count": "Could not determine the number of episodes from AniList",
        "dl_lang_pl_sub": "Polish (PL Subtitles)",
        "dl_lang_en_sub": "English (EN Subtitles)",
        "dl_lang_en_dub": "English (EN Dubbing)",
        "dl_prompt_lang": "Select preferred language version for downloaded files: ",
        "dl_qual_best": "Best available (Default)",
        "dl_prompt_qual": "Select preferred video quality for download: ",
        "dl_folder_pl": "[PL]",
        "dl_folder_en_sub": "[EN Sub]",
        "dl_folder_en_dub": "[EN Dub]",
        "dl_info_prep": "[INFO] Preparing to download {} (Selected {} eps)...",
        "dl_info_ver": "[INFO] Selected version: {}",
        "dl_info_qual": "[INFO] Selected quality: {}",
        "dl_info_loc": "[INFO] Save location: {}",
        "dl_err_no_src": "\n[ERROR] No sources found in the selected language for episode {}. Skipping...",
        "dl_ep_file_prefix": " - Episode",
        "dl_scan": "[*] Scanning source qualities for episode {}...",
        "dl_err_all_dead": "\n[ERROR] None of the sources for episode {} are working.",
        "dl_try_dl": "[*] Trying to download from: {} [{}] (Source {}/{})...",
        "dl_prog_vid": "Downloading ep. {} [bold yellow](VIDEO track)",
        "dl_prog_aud": "Downloading ep. {} [bold yellow](AUDIO track)",
        "dl_prog_done": "[bold green]Completed ep. {}!",
        "dl_prog_err": "[bold red]Error downloading ep. {}!",
        "dl_ytdlp_err": "\n   [yt-dlp error details]: {}",
        "dl_err_failed_all": "[ERROR] All sources for episode {} failed.",
        "dl_finished_all": "\n[FINISHED] Download process for series {} has ended!",
        "dl_enter_to_return": "Press Enter to return...",

        # local_lib
        "lib_err_no_dir": "[ERROR] Your download folder does not exist yet ({}).",
        "lib_err_no_anime": "You need to download some anime first!",
        "lib_enter_to_return": "Press Enter to return to the menu...",
        "lib_info_empty": "[INFO] Your download folder is empty.",
        "lib_prompt_series": "Select a series from the disk: ",
        "lib_err_no_vids": "No video files found in folder {}.",
        "lib_watch_auto": "Watch automatically",
        "lib_back_to_series": "Back to series selection",
        "lib_prompt_ep": "Select episode ({}): ",
        "lib_auto_playing": "Auto-playing: {}",
        "lib_mpv_info": "Press 'Q' inside the MPV window or close it to stop watching and return to the menu.",
        "lib_auto_interrupted": "\n[INFO] Auto-play interrupted.",
        "lib_press_enter": "Press Enter...",
        "lib_err_no_mpv": "[ERROR] mpv player not found!",
        "lib_playing_disk": "Playing from disk: {}",

        # player
        "player_err": "[ERROR]",
        "player_req_install": "For the program to work, you must install",
        "player_lycoris_ok": "[+] Success! Direct video link found.",
        "player_lycoris_fail": "[-] Failed to decode the link. Attempting default playback...",
        "player_unknown_anime": "Unknown Anime",
        "player_ep": "Episode",
        "player_warn": "[WARNING]",
        "player_req_mega": "To watch from this source, you must install",

        # ui_utils
        "ui_desc_header": "AniList Description:",
        "ui_no_chafa": "Tool 'chafa' is missing to display covers.",
        "ui_ctrl_c": "Ctrl+C = Back / Main Menu",
        "ui_not_found": "Not found in the list, please search again",

        # run
        "run_env_check": "[INFO] Checking environment and dependencies...",
        "run_yt_installed_old": "Installed (Yours: {} | Latest: {})",
        "run_yt_update_rec": "    [!] Update recommended using command: ({}), some sources may not work!",
        "run_yt_installed_ok": "Installed (Version: {} - Up to date!)",
        "run_yt_installed": "Installed (Version: {})",
        "run_yt_missing": "MISSING! Video playback and downloading will not work.",
        "run_mpv_installed": "Installed (Version: {})",
        "run_mpv_missing": "MISSING! Video playback will not work.",
        "run_chafa_installed": "Installed (Version: {} | Cover display)",
        "run_chafa_missing": "Missing [Cover display]",
        "run_mega_installed": "Installed (Version: {})",
        "run_mega_missing": "Missing (Playback from Mega.nz sources)",
        "run_upd_current": "Program version: ",
        "run_upd_latest": "Latest version:",
        "run_upd_avail": "A new version of otacli is available!",
        "run_upd_prompt": "Do you want to download and install the update automatically now?",
        "run_upd_manual": "Update details and instructions can be found here:",
        "run_upd_dl": "\n[*] Downloading update from GitHub... This will just take a moment.",
        "run_upd_dl_ok": "[+] Downloaded successfully. Starting installation...",
        "run_upd_err": "[-] Error during update download/installation: {}",
        "run_enter_cont": "Press Enter to continue...",

        # stats - pory dnia i nawyki
        "stat_night": "Night Owl (22-04)",
        "stat_early": "Early Bird (04-12)",
        "stat_chill": "Afternoon Chill (12-17)",
        "stat_evening": "Evening Watch (17-22)",
        "stat_none": "None",
        "stat_no_data": "No data",
        
        # stats - tabele i etykiety
        "stat_lbl_rank": "Current Rank:",
        "stat_lbl_otacli_eps": "Watched in otacli:",
        "stat_lbl_otacli_time": "otacli watch time:",
        "stat_lbl_total_eps": "Total episodes watched:",
        "stat_lbl_total_time": "Total watch time:",
        "stat_lbl_last": "Last watched:",
        
        "stat_unit_eps": "eps.",
        "stat_lbl_marathon": "Lifetime marathon (1 day):",
        "stat_lbl_weekly": "Weekly average:",
        "stat_lbl_prime_time": "Prime watch time:",
        "stat_lbl_net_disk": "Network vs Disk:",
        "stat_net_str": "net",
        "stat_disk_str": "disk",
        
        "stat_lbl_completed_rest": "Completed vs Rest:",
        "stat_lbl_planning": "Backlog (Planning):",
        "stat_lbl_oldest_queue": "Oldest in queue:",
        "stat_lbl_top_genres": "Top Genres (Top 3):",
        "stat_lbl_mean_score": "Mean score given:",
        "stat_lbl_al_status": "Connection status:",
        "stat_al_no_data": "No data from AniList",
        
        "stat_lbl_share": "otacli share in history:",
        "stat_lbl_size": "Disk space used:",
        "stat_lbl_install": "otacli installed:",
        "stat_lbl_age": "Profile age:",
        "stat_days": "days",
        
        # stats - panele
        "stat_panel_profile": "🎬 Your Profile",
        "stat_panel_habits": "🧠 Your Habits (otacli)",
        "stat_panel_anilist": "☁️ Account Stats (AniList)",
        "stat_panel_library": "📁 Library & Data",
        "stat_panel_legend": "🏆 Rank Legend",
        
        # stats - legenda rang (wymagania czasowe)
        "stat_req_hours": "hrs.",
        "stat_return_prompt": "Press enter to return to the main menu...",

        # ranks
        "rank_freshman": "Rookie",
        "rank_viewer": "Viewer",
        "rank_novice": "Novice",
        "rank_disciple": "Disciple",
        "rank_squire": "Squire",
        "rank_genin": "Genin",
        "rank_chuunin": "Chuunin",
        "rank_jonin": "Jonin",
        "rank_samurai": "Samurai",
        "rank_ronin": "Ronin",
        "rank_shinobi": "Shinobi",
        "rank_otaku": "Otaku",
        "rank_scout": "Scout",
        "rank_hunter": "Hunter",
        "rank_assassin": "Assassin",
        "rank_supernova": "Supernova",
        "rank_captain": "Captain",
        "rank_master": "Master",
        "rank_hero": "Hero",
        "rank_archmage": "Archmage",
        "rank_king": "King",
        "rank_emperor": "Emperor",
        "rank_deity": "Deity",
        "rank_titan": "Titan",
        "rank_hikikomori": "Hikikomori",

        "det_trailer": "Watch trailer",
        "trailer_loading": "[INFO] Loading trailer in MPV player...",

        "menu_notifications": "Notifications ({})",
        "notif_title": "Notifications",
        "notif_empty": "No notification history.",
        "notif_clear": "Clear notification history",
        "notif_new_ep": "New episode: {} (Ep. {}) is now available!",
    }
}

LANG = "en"


def t(key: str) -> str:
    """Returns UI text for the given key."""
    return TEXTS[LANG].get(key, key)