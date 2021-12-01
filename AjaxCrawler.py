
import urllib.request   as request 
import json
src="https://medium.com"
src="https://medium.com/_/graphql" 
#加header
header={
        # "origin": "https://medium.com",#加cookie
        # "sec-fetch-site": "same-origin",
        # "referer":"https://medium.com/",
        # "cookie":"uid=lo_7fb98e28889e; sid=1:LA4A9FuMCee9yYbWXZhFQyGUrct4xNMC0TBvjI7ESuCcb5FGqKresV64FwD+7ZLO; optimizelyEndUserId=lo_7fb98e28889e; _ga=GA1.2.333326154.1636962913; __cfruid=2fc2905ef18f06de8d5dd13bf973c78e6f3a4e29-1638262811; _gid=GA1.2.2117185590.1638262821; g_state={\"i_p\":1638867646673,\"i_l\":3}; _gat=1; _dd_s=rum=0&expire=1638264185900",
        # "graphql-operation": "ExtendedFeedQuery",
        "content-type": "application/json",
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"    
    }
requestPayload={"operationName":"WebRankedModulesScreen","variables":{},"query":"query WebRankedModulesScreen {\n  webRankedModules(\n    options: {recommendationSurface: MODULAR_WEB_HP, icelandVersion: ICELAND_GENERAL_RELEASE}\n  ) {\n    ... on Modules {\n      modules {\n        ...BasePostModuleData\n        ...RecentlyUpdatedModuleData\n        ...FollowedStoriesRankedModuleData\n        ...HomeFeedModuleData\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment BasePostModuleData on BaseRankedModule {\n  metadata {\n    ...RankedModuleMetadataData\n    __typename\n  }\n  entities: items {\n    ... on ModuleItemPost {\n      __typename\n      post {\n        ...PostListModulePostPreviewData\n        __typename\n        id\n      }\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment RankedModuleMetadataData on RankedModuleMetadata {\n  type\n  feedId\n  sourceEncoding\n  __typename\n}\n\nfragment PostListModulePostPreviewData on Post {\n  id\n  firstPublishedAt\n  readingTime\n  createdAt\n  mediumUrl\n  previewImage {\n    id\n    __typename\n  }\n  title\n  collection {\n    id\n    domain\n    slug\n    name\n    navItems {\n      url\n      __typename\n    }\n    logo {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    __typename\n  }\n  creator {\n    id\n    name\n    username\n    imageId\n    mediumMemberAt\n    ...userUrl_user\n    __typename\n  }\n  visibility\n  isProxyPost\n  isLocked\n  ...HomeFeedItem_post\n  ...HomeTrendingModule_post\n  __typename\n}\n\nfragment HomeFeedItem_post on Post {\n  __typename\n  id\n  title\n  firstPublishedAt\n  mediumUrl\n  collection {\n    id\n    name\n    domain\n    logo {\n      id\n      __typename\n    }\n    __typename\n  }\n  creator {\n    id\n    name\n    username\n    imageId\n    mediumMemberAt\n    __typename\n  }\n  previewImage {\n    id\n    __typename\n  }\n  previewContent {\n    subtitle\n    __typename\n  }\n  readingTime\n  tags {\n    ...TopicPill_tag\n    __typename\n  }\n  ...BookmarkButton_post\n  ...CreatorActionOverflowPopover_post\n  ...PostPresentationTracker_post\n  ...PostPreviewAvatar_post\n}\n\nfragment TopicPill_tag on Tag {\n  __typename\n  id\n  displayTitle\n}\n\nfragment BookmarkButton_post on Post {\n  visibility\n  ...SusiClickable_post\n  ...AddToCatalogBookmarkButton_post\n  __typename\n  id\n}\n\nfragment SusiClickable_post on Post {\n  id\n  mediumUrl\n  ...SusiContainer_post\n  __typename\n}\n\nfragment SusiContainer_post on Post {\n  id\n  __typename\n}\n\nfragment AddToCatalogBookmarkButton_post on Post {\n  ...AddToCatalogBase_post\n  __typename\n  id\n}\n\nfragment AddToCatalogBase_post on Post {\n  id\n  viewerEdge {\n    catalogsConnection {\n      catalogsContainingThis(type: LISTS) {\n        catalogId\n        catalogItemIds\n        __typename\n      }\n      predefinedContainingThis {\n        catalogId\n        predefined\n        catalogItemIds\n        __typename\n      }\n      __typename\n    }\n    ...editCatalogItemsMutation_postViewerEdge\n    ...useAddItemToPredefinedCatalog_postViewerEdge\n    __typename\n    id\n  }\n  ...WithToggleInsideCatalog_post\n  __typename\n}\n\nfragment useAddItemToPredefinedCatalog_postViewerEdge on PostViewerEdge {\n  id\n  catalogsConnection {\n    predefinedContainingThis {\n      catalogId\n      version\n      predefined\n      catalogItemIds\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment editCatalogItemsMutation_postViewerEdge on PostViewerEdge {\n  id\n  catalogsConnection {\n    catalogsContainingThis(type: LISTS) {\n      catalogId\n      version\n      catalogItemIds\n      __typename\n    }\n    predefinedContainingThis {\n      catalogId\n      predefined\n      version\n      catalogItemIds\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment WithToggleInsideCatalog_post on Post {\n  id\n  viewerEdge {\n    catalogsConnection {\n      catalogsContainingThis(type: LISTS) {\n        catalogId\n        __typename\n      }\n      predefinedContainingThis {\n        predefined\n        __typename\n      }\n      __typename\n    }\n    __typename\n    id\n  }\n  __typename\n}\n\nfragment CreatorActionOverflowPopover_post on Post {\n  allowResponses\n  id\n  statusForCollection\n  isLocked\n  isPublished\n  clapCount\n  mediumUrl\n  pinnedAt\n  pinnedByCreatorAt\n  curationEligibleAt\n  mediumUrl\n  responseDistribution\n  visibility\n  ...useIsPinnedInContext_post\n  pendingCollection {\n    id\n    name\n    creator {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    domain\n    slug\n    __typename\n  }\n  creator {\n    id\n    ...MutePopoverOptions_creator\n    ...auroraHooks_publisher\n    __typename\n  }\n  collection {\n    id\n    name\n    creator {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    domain\n    slug\n    ...MutePopoverOptions_collection\n    ...auroraHooks_publisher\n    __typename\n  }\n  ...ClapMutation_post\n  ...NewsletterV3EmailToSubscribersMenuItem_post\n  __typename\n}\n\nfragment MutePopoverOptions_creator on User {\n  id\n  __typename\n}\n\nfragment MutePopoverOptions_collection on Collection {\n  id\n  __typename\n}\n\nfragment ClapMutation_post on Post {\n  __typename\n  id\n  clapCount\n  ...MultiVoteCount_post\n}\n\nfragment MultiVoteCount_post on Post {\n  id\n  ...PostVotersNetwork_post\n  __typename\n}\n\nfragment PostVotersNetwork_post on Post {\n  id\n  voterCount\n  recommenders {\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment useIsPinnedInContext_post on Post {\n  id\n  collection {\n    id\n    __typename\n  }\n  pendingCollection {\n    id\n    __typename\n  }\n  pinnedAt\n  pinnedByCreatorAt\n  __typename\n}\n\nfragment auroraHooks_publisher on Publisher {\n  __typename\n  ... on Collection {\n    isAuroraEligible\n    isAuroraVisible\n    viewerEdge {\n      id\n      isEditor\n      __typename\n    }\n    __typename\n    id\n  }\n  ... on User {\n    isAuroraVisible\n    __typename\n    id\n  }\n}\n\nfragment NewsletterV3EmailToSubscribersMenuItem_post on Post {\n  id\n  creator {\n    id\n    newsletterV3 {\n      id\n      subscribersCount\n      __typename\n    }\n    __typename\n  }\n  isPublishToEmail\n  isNewsletter\n  __typename\n}\n\nfragment PostPresentationTracker_post on Post {\n  id\n  visibility\n  previewContent {\n    isFullContent\n    __typename\n  }\n  collection {\n    id\n    slug\n    __typename\n  }\n  __typename\n}\n\nfragment PostPreviewAvatar_post on Post {\n  __typename\n  id\n  collection {\n    id\n    name\n    ...CollectionAvatar_collection\n    __typename\n  }\n  creator {\n    id\n    username\n    name\n    ...UserAvatar_user\n    ...userUrl_user\n    __typename\n  }\n}\n\nfragment CollectionAvatar_collection on Collection {\n  name\n  avatar {\n    id\n    __typename\n  }\n  ...collectionUrl_collection\n  __typename\n  id\n}\n\nfragment collectionUrl_collection on Collection {\n  id\n  domain\n  slug\n  __typename\n}\n\nfragment UserAvatar_user on User {\n  __typename\n  id\n  imageId\n  mediumMemberAt\n  name\n  username\n  ...userUrl_user\n}\n\nfragment userUrl_user on User {\n  __typename\n  id\n  customDomainState {\n    live {\n      domain\n      __typename\n    }\n    __typename\n  }\n  hasSubdomain\n  username\n}\n\nfragment HomeTrendingModule_post on Post {\n  id\n  ...HomeTrendingPostPreview_post\n  __typename\n}\n\nfragment HomeTrendingPostPreview_post on Post {\n  id\n  title\n  mediumUrl\n  readingTime\n  firstPublishedAt\n  ...PostPreviewAvatar_post\n  ...PostPresentationTracker_post\n  __typename\n}\n\nfragment RecentlyUpdatedModuleData on RecentlyUpdatedEntitiesRankedModule {\n  metadata {\n    ...RankedModuleMetadataData\n    __typename\n  }\n  items {\n    ...RecentlyUpdatedEntityData\n    __typename\n  }\n  __typename\n}\n\nfragment RecentlyUpdatedEntityData on RankedModuleUpdatedFollowedEntity {\n  entity {\n    __typename\n    ... on Collection {\n      id\n      name\n      avatar {\n        id\n        __typename\n      }\n      domain\n      slug\n      __typename\n    }\n    ... on User {\n      id\n      name\n      username\n      imageId\n      mediumMemberAt\n      ...userUrl_user\n      __typename\n    }\n  }\n  updatesCount\n  updatesCountText\n  __typename\n}\n\nfragment FollowedStoriesRankedModuleData on FollowedStoriesRankedModule {\n  metadata {\n    ...RankedModuleMetadataData\n    __typename\n  }\n  items {\n    ...FollowedStoryPreviewData\n    __typename\n  }\n  __typename\n}\n\nfragment FollowedStoryPreviewData on RankedModuleFollowedStoriesItem {\n  post {\n    __typename\n    id\n    title\n    readingTime\n    mediumUrl\n    firstPublishedAt\n    previewImage {\n      id\n      __typename\n    }\n    previewContent {\n      isFullContent\n      subtitle\n      __typename\n    }\n    creator {\n      id\n      name\n      imageId\n      mediumMemberAt\n      username\n      ...userUrl_user\n      __typename\n    }\n    collection {\n      id\n      name\n      avatar {\n        id\n        __typename\n      }\n      domain\n      slug\n      __typename\n    }\n    isProxyPost\n    visibility\n    isLocked\n    ...BookmarkButton_post\n    ...CreatorActionOverflowPopover_post\n  }\n  __typename\n}\n\nfragment HomeFeedModuleData on ExtendedFeedRankedModule {\n  metadata {\n    ...RankedModuleMetadataData\n    __typename\n  }\n  feedItems {\n    post {\n      ...PostListModulePostPreviewData\n      __typename\n    }\n    postId\n    metadata {\n      reason\n      postFeedReason\n      topicId\n      topic {\n        id\n        name\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  extendedFeedItems {\n    postId\n    metadata {\n      reason\n      postFeedReason\n      topicId\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n"}
def setheader(_src, _header,_data):
    _req= request.Request(_src, headers=_header, data=json.dumps(_data) .encode("utf-8"))
    return _req

def getUrldata(_req):
    with request.urlopen(_req) as response :
        _data= response.read().decode("utf-8") 
    return _data    
def getDOM(_req):  
    import bs4
    _root = bs4.BeautifulSoup(getUrldata(_req), "html.parser")
    # print(root)
    # print(_root.title.string)
    return _root


#抓回上頁的連結
def getbacklink(soup):
    back_tags=soup.find("a",string="‹ 上頁")
    # print(back_tags)
    # print(back_tags["href"])
    return back_tags["href"]
def getdata(soup):
    div_tags=soup.find("div",class_="title")
    # print(div_tags)
    # print(div_tags.a.string)
    return div_tags.a.string

def getalldata(soup):
    #抓標題
    div_tags=soup.find_all("div",class_="title")
    datalist=list()
    for tag in div_tags:
        if tag.a!= None:
            # print(len(datalist))
            # datalist.append(tag.a.string)
            datalist[len(datalist):]=[tag.a.string]
            # print(tag.a.string)
    return datalist
    
def printlist(_data):
    _counter=0
    for i in _data:
        print(str(_counter)+":"+str(i))
        _counter+=1


def write2tmp(_str):       
    with open("tmp.txt", mode="w", encoding="utf-8") as tmpfile:
        tmpfile.write(_str)

def getData(_src, _header,_data):
    _req=setheader(_src, _header,_data)   
    _root=getUrldata(_req)
    # root=getDOM(_req)
    # write2tmp(root)
    _result=list()
    _result=json.loads(_root)
    # print(result[data][webRankedModules][modules])
    return _result

result= getData(src, header, requestPayload)
print(result["data"]["webRankedModules"]["modules"][0]["items"][0]["post"]["title"])
items=result["data"]["webRankedModules"]["modules"][0]["items"]
counter=0
for i in items:
    counter+=1
    print(str(counter) +": " +i["post"]["title"])
